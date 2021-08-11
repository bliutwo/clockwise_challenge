#include <bits/stdc++.h>
using namespace std;

string printVector(vector<int>& v) {
    string s{};
    s += "{ ";
    for (size_t i = 0; i < v.size(); i++) {
        s += v[i];
        s += " ";
    }
    s += "}";
    return s;
}

void printVectorOfVectors(vector<vector<int>>& v) {
    cout << "{ " << endl;
    for (size_t i = 0; i < v.size(); i++) {
        cout << printVector(v[i]) << endl;
    }
    cout << "}";
}

void solve(vector<vector<vector<int>>> meetings) {
    for (auto meetings
}

int main() {
    vector<vector<vector<int>>> test_cases = {
        {{0,1,2},{1,2}},
        {{0,1},{0},{1}},
        {{0,1,2},{2,3}}
        // [[4,10],[3,4,12],[0,8,9,10,13],[1,5,7],[2,6],[9,4,10,11,12],[11,13]],
        // [[6,16,17],[8,9],[1],[7,14,9],[10,5],[2,7],[0,6,7,9],[10,11,5,13,15,16,17],[7,9],[5,9],[2,12,5,6,14,7,15,9],[10,5,14],[1,4,8],[1,3,9],[5]],
        // [[9,16,34],[10,13,18,20,23,28,30,31,32],[4,7,8,11,16,17,19,25,29,36,37],[0,2,23,28],[1,3,7,8,14,15,19,24,25,26,32],[12,28],[16,21,24,33,34],[5,6,10,15,16,17,21,22,24,27,33,34,35]]
    };

    solve(test_cases);

    return 0;
}
