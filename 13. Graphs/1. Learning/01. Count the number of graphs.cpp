/*Question:-

Count the number of undirected graphs that can be formed with n vertices.

Approach:-
- calculate the number of edges with formula n*n-1/2
- return pow(2,edges) 

Complexity Analysis:-

Time Complexity = O(1)
Space Complexity = O(1)
*/


#include <bits/stdc++.h>
using namespace std;
int countingGraphs(int n)
{
    int edges = (n*(n-1))/2;
    return pow(2,edges);
}

int main() {
    // TODO: Extract test cases from the examples above
    
    // Call your function: countingGraphs()
    // Print result:
    // cout << "Result: " << result << endl;
    
    return 0;
}

