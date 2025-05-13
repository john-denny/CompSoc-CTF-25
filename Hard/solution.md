# Solution to Medium Web Exploitation
Flag - CompSoc{CATHAL_LAWLOR_FANCLUB_69420}
When Giving the link to this challenge, give the users 
http://address/view?file=index.html/

1. If you view the contents of style.css it has a hidden message
2. The hidden message is TODO: Secure /execute?cmd= (GET) endpoint.
3. This can be used to Remote Code Execution, the first 30 characters of which will be displayed to the user in that window
4. They can use this to analyse the file structure, discover the file bratach.txt and `cat` it