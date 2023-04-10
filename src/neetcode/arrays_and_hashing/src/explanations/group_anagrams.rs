struct Solution;

use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        /*
         * 単語を構成するアルファベットの出現回数を HashMap で管理する
         * key が配列 (u8 型、長さは 26) で、アルファベットの出現回数パターン
         * value が該当する単語のベクター
         */
        let mut map: HashMap<[u8; 26], Vec<String>> = HashMap::new();

        for s in strs {
            // 長さ 26 の配列を定義、すべての要素を u8 型の 0 で初期化。要素数は変動しないので Vector ではなく array で OK
            let mut key = [0_u8; 26];

            for c in s.chars() {
                // ASCII value "a" は 80 の数値なので、それを引いてあげると 0, 1, 2 ... とキリのいい数値になる
                key[c as usize - 'a' as usize] += 1;
            }

            if let Some(vals) = map.get_mut(&key) {
                // 単語のベクターに追加
                vals.push(s);
            } else {
                // 新しいパターン追加、単語のベクター作成
                map.insert(key, vec![s]);
            }
        }

        map.into_values().collect()
    }
}

struct Case {
    expected: Vec<Vec<String>>,
    strs: Vec<String>,
}

struct TestCase {
    data: Vec<Case>,
}

impl TestCase {
    fn new() -> Self {
        TestCase {
            data: vec![
                Case {
                    expected: vec![
                        vec![String::from("bat")],
                        vec![
                            String::from("eat"),
                            String::from("tea"),
                            String::from("ate"),
                        ],
                        vec![String::from("tan"), String::from("nat")],
                    ],
                    strs: vec!["eat", "tea", "tan", "ate", "nat", "bat"]
                        .iter()
                        .map(|s| s.to_string())
                        .collect(),
                },
                Case {
                    expected: vec![vec![String::from("")]],
                    strs: vec![String::from("")],
                },
                Case {
                    expected: vec![vec![String::from("a")]],
                    strs: vec![String::from("a")],
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
    let test_cases = TestCase::new();
    for case in test_cases.data.into_iter() {
        // 要素は順不同なので HashSet にして比較する
        let set1: HashSet<_> = Solution::group_anagrams(case.strs).into_iter().collect();
        let set2: HashSet<_> = case.expected.into_iter().collect();
        assert_eq!(set1, set2);
    }
}
