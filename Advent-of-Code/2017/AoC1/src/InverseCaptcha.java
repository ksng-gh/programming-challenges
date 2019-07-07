public class InverseCaptcha {
    /*
    For the first part
     */
    public static int decode(String input){
        int pos = 0;
        int sum = 0;

        if(input.length() > 2 && (input.charAt(pos) == input.charAt(input.length() - 1))){
            sum = Character.getNumericValue(input.charAt(pos));
        }

        while(pos < input.length() - 1){
            if(input.charAt(pos) == input.charAt(pos + 1)){
                sum += Character.getNumericValue(input.charAt(pos));
            }

            pos++;
        }
        return sum;
    }
    /*
    For the second part
     */

    public static int decodeHalfway(String input){
        int beginPos = 0;
        int halfwayPos = (input.length())/2;
        int sum = 0;

        while(beginPos < input.length()){

            if(input.charAt(beginPos) == input.charAt(halfwayPos)){
                sum += Character.getNumericValue(input.charAt(beginPos));
            }

            beginPos++;
            halfwayPos++;

            if(halfwayPos == input.length()){
                halfwayPos = 0;
            }
        }
        return sum;
    }


}
