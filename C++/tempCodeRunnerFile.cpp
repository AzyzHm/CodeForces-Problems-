#include <iostream>
#include <vector>
#include <string>

int main() {
    int t;
    std::cin >> t;
    std::vector<std::string> results;
    results.reserve(t); // Reserve space to avoid multiple allocations

    for (int i = 0; i < t; ++i) {
        std::string n;
        std::cin >> n;
        if (n.size() >= 4 && n.substr(0, 2) == "10" && n.find_first_not_of('0', 2) == std::string::npos) {
            results.push_back("Yes");
        } else {
            results.push_back("No");
        }
    }

    for (const auto& result : results) {
        std::cout << result << std::endl;
    }

    return 0;
}