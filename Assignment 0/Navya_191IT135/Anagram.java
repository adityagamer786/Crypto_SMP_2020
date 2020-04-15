import java.util.*;
class Anagram
{
    public static void main(String args[])
    {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter String1: ");
        String s1 = scan.nextLine();
        System.out.println("Enter String2: ");
        String s2 = scan.nextLine();
        int[] arr1 = new int[26];
        int[] arr2 = new int[26];
        check(arr1,s1);
        check(arr2,s2);
        int i;
        for(i = 0; i < 26; i++)
        {
            if(arr1[i]!=arr2[i])break;
        }
        if(i == 26)System.out.println("It is an anagram.");
        else System.out.println("It is not an anagram.");
    }
    static void check(int[] a,String s)
    {
       int i;
       for(i=0;i<s.length();i++)
       {
           int ch = s.charAt(i)-96;
           if(ch == 1)
           {
               a[1]++;
               continue;
           }
           int c1 = checkPrime(ch);
           int c2 = checkPrime(26-ch);
           if(c1 == 0&&c2 == 0)
           {
               a[ch]++;
               a[26-ch]++;
           }
       }
    }
    static int checkPrime(int x)
    {
        int flag = 0;
        for(int i = 2; i<=x/2; i++)
        {
            if(x%i==0)
            {
                flag = 1;
                break;
            }
        }
        return flag;
    }
}  