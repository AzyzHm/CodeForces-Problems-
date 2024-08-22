#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;
    vector<string> results;
    while (t--) {
        vector<string> board(8);
        string blank_line;
        cin >> ws; // To consume the blank line before each test case

        for (int i = 0; i < 8; ++i) {
            getline(cin, board[i]);
        }

        // Search for the bishop's position
        for (int i = 1; i < 7; ++i) {
            for (int j = 1; j < 7; ++j) {
                if (board[i][j] == '#' &&
                    board[i - 1][j - 1] == '#' &&
                    board[i - 1][j + 1] == '#' &&
                    board[i + 1][j - 1] == '#' &&
                    board[i + 1][j + 1] == '#') {
                    results.push_back(to_string(i + 1) + " " + to_string(j + 1));
                    break;
                }
            }
        }
    }
    for(auto result : results) {
        cout << result << endl;
    }

    return 0;
}
