// solution still incomplete
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int solver(const std::string& a, const std::string& b, int s, int e) {
    if (s == e) {
        if (a[s-1] == b[s-1]) {
            return 0;
        } else {
            return 1;
        }
    }
    s -= 1;

    std::string first = a.substr(s, e - s);
    std::string second = b.substr(s, e - s);

    std::sort(first.begin(), first.end());
    std::sort(second.begin(), second.end());

    int i = 0, j = 0;
    int unmatched = 0;

    while (i < first.size() && j < second.size()) {
        if (first[i] == second[j]) {
            ++i;
            ++j;
        } else if (first[i] < second[j]) {
            ++i;
            ++unmatched;
        } else {
            ++j;
        }
    }

    unmatched += first.size() - i;

    return unmatched;
}


int main() {
	int t;
	cin >> t;
	vector<int> results;
	for (int i = 0; i < t; ++i) {
		int n, q;
		cin >> n >> q;
		string a, b;
		cin >> a >> b;
		vector<pair<int, int>> queries;
		for (int j = 0; j < q; ++j) {
			int s, e;
			cin >> s >> e;
			queries.push_back({s, e});
		}
		for (const auto& query : queries) {
			int s = query.first;
			int e = query.second;
			results.push_back(solver(a, b, s, e));
		}
	}
	for (const auto& r : results) {
		cout << r << endl;
	}
	return 0;
}