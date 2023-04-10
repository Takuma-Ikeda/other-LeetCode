use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        // 文字列の長さが違うなら確実に false
        if t.len() != s.len() {
            return false;
        }

        // key の型を char, value の型を i64 で型指定したので or_default() の初期値は 0 で推測される
        let mut map: HashMap<char, i64> = HashMap::new();

        // zip 関数で複数配列の要素を for 内で同時に扱える
        for (a, b) in s.chars().zip(t.chars()) {
            *map.entry(a).or_default() += 1;
            *map.entry(b).or_default() -= 1;
        }

        // into_values で HashMap すべての値を取り出して、新しい所有権をもった Vec を生成 ※ HashMap の中身は空になる
        // Vec の all メソッドは全ての要素が条件を満たせば true を返す
        map.into_values().all(|cnt| cnt == 0)
    }
}

struct Case {
    expected: bool,
    s: String,
    t: String,
}

struct TestCase {
    data: Vec<Case>,
}

impl TestCase {
    fn new() -> Self {
        TestCase {
            data: vec![
                Case {
                    expected: true,
                    s: String::from("anagram"),
                    t: String::from("nagaram"),
                },
                Case {
                    expected: false,
                    s: String::from("rat"),
                    t: String::from("car"),
                },
            ],
        }
    }
}

pub fn run() {
    execute();
}

#[test]
fn test() {
    execute();
}

fn execute() {
    let test_cases: TestCase = TestCase::new();
    for case in test_cases.data.into_iter() {
        assert_eq!(case.expected, Solution::is_anagram(case.s, case.t))
    }
}
