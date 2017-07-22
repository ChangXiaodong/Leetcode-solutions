import java.util.ArrayList;
import java.util.List;

/**
 * Created by chang on 2017-04-30.
 */
public class Solution {
    public List<List<Integer>> dfs(List<Boolean> used, int[] nums, List<Integer> buf, List<List<Integer>> res){
        if(buf.size() == nums.length){
            res.add(buf);
        }
        for(int i=0;i<nums.length;i++){
            if(!used.get(i)){
                used.set(i, true);
                buf.add(nums[i]);
                dfs(used, nums, buf, res);
                buf.remove(i);
                used.set(i, false);
            }
        }
        return res;
    }

    public List<List<Integer>> permute(int[] nums) {
        List<Boolean> used = new ArrayList<>();
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> buf = new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            used.add(false);
        }

        if(nums.length==0){
            return res;
        }
        dfs(used, nums, buf, res);
        return res;

    }
}