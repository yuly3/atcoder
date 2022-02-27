// -*- coding:utf-8-unix -*-

use proconio::input;

fn solve() {
    input! {
        n: usize,
        mut uv: [(usize, usize); n - 1],
    }
    println!("Hello, Atcoder!");
}

fn main() {
    // In order to avoid potential stack overflow, spawn a new thread.
    let stack_size = 104_857_600; // 100 MB
    let thd = std::thread::Builder::new().stack_size(stack_size);
    thd.spawn(|| solve()).unwrap().join().unwrap();
}
