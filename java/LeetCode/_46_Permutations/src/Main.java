import java.util.ArrayList;
import java.util.List;

/**
 * Created by chang on 2017-04-30.
 */
public class Main {
    public void main(int args[]) {
        Solution solution = new Solution();
        List<List<Integer>> res = new ArrayList<>();
        int[] input = {1, 2, 3};
        res = solution.permute(input);
        for (int i = 0; i < res.size(); i++) {
            for (int j = 0; i < res.get(i).size(); j++) {
                System.out.print(res.get(i).get(j));
            }
        }
    }

}
