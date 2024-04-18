class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        
    int rows = grid.size();
    int cols = grid[0].size();
    int landCells = 0;
    int waterNeighbors = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == 1) {
                landCells++;
                if (i > 0 && grid[i-1][j] == 1) waterNeighbors++;
                if (i < rows-1 && grid[i+1][j] == 1) waterNeighbors++;
                if (j > 0 && grid[i][j-1] == 1) waterNeighbors++;
                if (j < cols-1 && grid[i][j+1] == 1) waterNeighbors++;
            }
        }
    }
    return landCells * 4 - waterNeighbors;
}
};
