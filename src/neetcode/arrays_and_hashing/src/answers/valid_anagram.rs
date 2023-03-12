use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut hashmap = HashMap::new();
        for c in s.chars() {
            if hashmap.get(&c).is_none() {
                hashmap.insert(c, 1);
                continue;
            }

            let count = hashmap.get(&c).unwrap() + 1;
            hashmap.insert(c, count);
        }

        for c in t.chars() {
            if hashmap.get(&c).is_none() {
                return false;
            }

            let count = hashmap.get(&c).unwrap() - 1;

            if count < 0 {
                return false;
            }

            hashmap.insert(c, count);
        }

        for count in hashmap.values() {
            if count != &0 {
                return false;
            }
        }

        true
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
                }
            ]
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
