import argparse
import os
import subprocess
from enum import Enum, auto
from glob import glob
from shutil import copyfile, copytree

RS_PROJECT_DIR = os.path.join("C:\\", "Users", "{}", "atcoder", "RustProject")


class Extention(Enum):
    py = auto()
    nim = auto()
    rs = auto()


def copy_template(
    contest_name: str, extention: str, dst_src_file_dir: str
) -> None:
    problem_num = 8 if contest_name.lower() in ("abc",) else 6
    for i in range(problem_num):
        new_problem = chr(ord('A') + i) + '.' + extention
        copyfile(
            os.path.join(".", "template." + extention),
            os.path.join(dst_src_file_dir, new_problem),
        )
    return


def make_contest_dir_rs(contest_name: str, contest_num: str) -> None:
    new_contest_dir = (
        os.path.join(
            ".", contest_name.upper(), contest_name.upper() + contest_num
        )
        if contest_num != "" else
        os.path.join(".", "other", contest_name)
    )
    if not os.path.exists(new_contest_dir):
        os.mkdir(new_contest_dir)
    elif os.path.exists(os.path.join(new_contest_dir, "rust-toolchain")):
        print('This contest is already there.')
        return

    print(RS_PROJECT_DIR)
    rs_project_dir = input("Please complete the directory name: ")
    dst_target_dir = os.path.join(
        "C:\\",
        "Users",
        "{}",
        "atcoder",
        contest_name.upper(),
        contest_name.upper() + contest_num,
        "target",
    ).format(rs_project_dir)
    rs_project_dir = RS_PROJECT_DIR.format(rs_project_dir)
    if not os.path.exists(rs_project_dir):
        print(f"Rust Project Directory not found: {rs_project_dir}")
        return

    print("Making " + new_contest_dir)
    rust_project_items = glob(os.path.join(".", "RustProject", "*"))
    for item in rust_project_items:
        base_name = os.path.basename(item)
        if base_name == "target":
            continue
        if os.path.isfile(item):
            copyfile(item, os.path.join(new_contest_dir, base_name))
        elif os.path.isdir(item):
            copytree(item, os.path.join(new_contest_dir, base_name))

    src_target_dir = os.path.join(rs_project_dir, "target")
    _ = subprocess.Popen(
        f"mklink /J \"{dst_target_dir}\" \"{src_target_dir}\"",
        shell=True,
        stderr=subprocess.PIPE,
    )

    """
    stderr = comp_process.communicate()[1]
    stderr = stderr.decode("utf-8", errors="backslashreplace")
    stderr = (
        stderr
        .encode()
        .decode("unicode_escape")
        .encode("raw_unicode_escape")
        .decode("shift_jis")
    )
    print(stderr)
    """

    copy_template(
        contest_name, "rs", os.path.join(new_contest_dir, "src", "bin")
    )

    print("Done")
    print("Please edit Cargo.toml")
    return


def make_contest_dir(contest_name, contest_num, extention):
    if extention == Extention.rs.name:
        make_contest_dir_rs(contest_name, contest_num)
        return
    new_contest_dir = (
        os.path.join(
            ".", contest_name.upper(), contest_name.upper() + contest_num
        )
        if contest_num != "" else
        os.path.join(".", "other", contest_name)
    )
    if os.path.exists(new_contest_dir):
        print('This contest is already there.')
        return

    print('Making ' + new_contest_dir)
    os.mkdir(new_contest_dir)
    copy_template(contest_name, extention, new_contest_dir)
    print("Done")
    return


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('contest_name')
    parser.add_argument('-n', '--contest_num', default='')
    parser.add_argument('-e', '--extention', default=Extention.nim.name)

    return parser.parse_args()


def main():
    exe_args = get_args()

    contest_num = exe_args.contest_num
    if contest_num != '':
        contest_num = contest_num.zfill(3)
    if all(it.name != exe_args.extention for it in Extention):
        print("extention: ", list(Extention))
        return

    make_contest_dir(exe_args.contest_name, contest_num, exe_args.extention)
    return


if __name__ == '__main__':
    main()
