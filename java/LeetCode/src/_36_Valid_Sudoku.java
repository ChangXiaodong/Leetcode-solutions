/**
 * Created by xiaoxiami on 2017/4/29.
 */

import java.util.HashSet;


public class _36_Valid_Sudoku {


    public static boolean rowValid(char[][] board) {
        HashSet<Character> buf = new HashSet<Character>();
        for (int i = 0; i < 9; i++) {
            buf.clear();
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    if ((board[i][j] > '9') || board[i][j] < '0') {
                        return false;
                    }
                    if (buf.contains(board[i][j])) {
                        return false;
                    } else {
                        buf.add(board[i][j]);
                    }
                }
            }
        }
        return true;
    }

    public static boolean colValid(char[][] board) {
        HashSet<Character> buf = new HashSet<Character>();
        for (int j = 0; j < 9; j++) {
            buf.clear();
            for (int i = 0; i < 9; i++) {
                if (board[i][j] != '.') {
                    if ((board[i][j] > '9') || board[i][j] < '0') {
                        return false;
                    }
                    if (buf.contains(board[i][j])) {
                        return false;
                    } else {
                        buf.add(board[i][j]);
                    }
                }

            }
        }
        return true;
    }

    public static boolean validGrig(char[][] board, int row, int col) {
        HashSet<Character> buf = new HashSet<Character>();
        for (int i = row; i < row + 3; i++) {
            for (int j = col; j < col + 3; j++) {
                if (board[i][j] != '.') {
                    if (board[i][j] > '9' || board[i][j] < '0') {
                        return false;
                    }
                    if (buf.contains(board[i][j])) {
                        return false;
                    } else {
                        buf.add(board[i][j]);
                    }
                }
            }
        }
        return true;
    }

    public static boolean isValidSudoku(char[][] board) {

        if (board == null) {
            return false;
        }
        int rows = board.length;
        int cols = board[0].length;
        if (!rowValid(board)) {
            return false;
        }
        if (!colValid(board)) {
            return false;
        }
        for (int i = 0; i < rows; i += 3) {
            for (int j = 0; j < cols; j += 3) {
                if (!validGrig(board, i, j)) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        char board[][] = {{'.', '8', '7', '6', '5', '4', '3', '2', '1'}, {'2', '.', '.', '.', '.', '.', '.', '.', '.'},
                {'3', '.', '.', '.', '.', '.', '.', '.', '.'}, {'4', '.', '.', '.', '.', '.', '.', '.', '.'},
                {'5', '.', '.', '.', '.', '.', '.', '.', '.'}, {'6', '.', '.', '.', '.', '.', '.', '.', '.'},
                {'7', '.', '.', '.', '.', '.', '.', '.', '.'}, {'8', '.', '.', '.', '.', '.', '.', '.', '.'},
                {'9', '.', '.', '.', '.', '.', '.', '.', '.'}};
        System.out.print(isValidSudoku(board));
    }

}


