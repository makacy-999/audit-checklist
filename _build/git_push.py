# -*- coding: utf-8 -*-
"""用 dulwich（纯 Python git）提交并通过 SSH 推送到 GitHub。
本机没有真正的 git（只有 Xcode shim），所以用这个替代。
SSH 私钥：~/.ssh/id_ed25519  公钥需由用户手动添加到 GitHub。
用法：
    python3 _build/git_push.py           # 提交 + 推送
    python3 _build/git_push.py --check   # 只测 SSH 身份，不提交
"""
import os, sys, stat

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REMOTE = "git@github.com:makacy-999/audit-checklist.git"
BRANCH = b"refs/heads/main"
AUTHOR = b"makacy-999 <makacy-999@users.noreply.github.com>"
KEY = os.path.expanduser("~/.ssh/id_ed25519")


def check_ssh():
    import paramiko
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        c.connect("github.com", username="git", key_filename=KEY,
                  timeout=20, allow_agent=False, look_for_keys=False)
    except paramiko.AuthenticationException:
        print("SSH 连通，但 GitHub 拒绝了这把钥匙 —— 公钥还没添加到 GitHub。")
        return False
    except Exception as e:
        print("SSH 连接失败:", type(e).__name__, e)
        return False
    finally:
        c.close()
    # 能连上就说明钥匙已被接受
    stdin, out, err = (None, None, None)
    return True


def collect(root):
    rel = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".git", "__pycache__", "node_modules")]
        for fn in filenames:
            if fn in (".DS_Store",):
                continue
            p = os.path.join(dirpath, fn)
            rel.append(os.path.relpath(p, root))
    return sorted(rel)


def main():
    from dulwich import porcelain
    from dulwich.repo import Repo

    if "--check" in sys.argv:
        print("SSH 身份:", "OK" if check_ssh() else "未授权")
        return 0 if check_ssh() else 1

    if not os.path.exists(os.path.join(REPO, ".git", "HEAD")):
        porcelain.init(REPO)
    repo = Repo(REPO)

    files = collect(REPO)
    if files:
        porcelain.add(repo, paths=files)
        msg = "审计应对 Check list: 8分类 / 47条目 / 112核对项（网页版 + Excel）".encode("utf-8")
        sha = porcelain.commit(repo, message=msg, author=AUTHOR, committer=AUTHOR)
        print("committed", sha.decode()[:10], "files:", len(files))
    else:
        sha = repo.refs[BRANCH]
        print("no change, reuse", sha.decode()[:10])

    # 统一到 main 分支
    refs = repo.refs
    for old in (b"refs/heads/master", b"HEAD~0"):
        pass
    if b"refs/heads/master" in refs:
        refs[BRANCH] = refs[b"refs/heads/master"]
        del refs[b"refs/heads/master"]
    if BRANCH not in refs:
        refs[BRANCH] = sha
    from dulwich.refs import SYMREF
    repo.refs.set_if_equals = None
    with open(os.path.join(REPO, ".git", "HEAD"), "wb") as f:
        f.write(b"ref: " + BRANCH + b"\n")

    print("pushing ->", REMOTE)
    try:
        porcelain.push(repo, REMOTE, BRANCH)
        print("PUSH OK")
        return 0
    except Exception as e:
        print("PUSH FAILED:", type(e).__name__, e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
