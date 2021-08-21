import java.util.*;
public class UniqueWords{
    public static String[] removeDupes(String[] input){
        HashSet<String> set = new HashSet<>();
        for(String word : input){
            if(!set.contains(word)){
                set.add(word);
            }
        }
        String[] clean = new String[set.size()];
        set.toArray(clean);
        return clean;
    }
    public static void main(String args[]){
        String[] input=new String[]{"alpha", "beta", "beta", "gamma", "gamma", "gamma", "delta", "alpha", "beta", "beta", "gamma", "gamma", "gamma", "delta"};
        String[] output=removeDupes(input);
        System.out.println(Arrays.toString(output));
    }
}