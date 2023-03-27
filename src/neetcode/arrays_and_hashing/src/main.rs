mod answers;
mod explanations;

fn main() {
    // 1. contains_duplicate
    answers::contains_duplicate::run();
    explanations::contains_duplicate::run();
    // 2. valid_anagram
    answers::valid_anagram::run();
    explanations::valid_anagram::run();
    // 3. two_sum
    answers::two_sum::run();
    explanations::two_sum::run();
    // 4. group_anagrams
    answers::group_anagrams::run();
    explanations::group_anagrams::run();
}
