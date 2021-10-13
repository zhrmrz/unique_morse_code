class Sol:
    def unique_morse_code(self, words):
        list=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",
        "...-",".--","-..-","-.--","--.."]
        morse=set()
        for word in words:
            transf=""
            for char in word:
                transf+=list[ord(char)-ord('a')]
            morse.add(transf)
        return len(morse)

if __name__ == '__main__':
    p = Sol()
    print(p.unique_morse_code(words=["gin","zen","gig","msg"]))
