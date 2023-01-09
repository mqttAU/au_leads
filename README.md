# au_leads
 
This python script allows the user to specify how many phone numbers they want to generate, generates those phone numbers without duplicates, saves those phone numbers to a .txt file, and gives the option to perform HLR validation on those numbers using the NumVerify API, and displays the carrier and validity information for each number in the text file. 

It then saves the validated phone numbers, along with the carrier and validity information, to the specified file and outputs a message indicating that the validated phone numbers were saved.  

Note that in order for this program to work, you will need to sign up for an API key from NumVerify. Replace API_KEY in the program with your own API key.

To do:
I was thinking of implementing a WhatsApp Filter and Facebook Filter to further validate numbers and filter out inactive ones as HLR validation can only provide if a mobile number has been registered, and may still be inactive. 

Nevertheless, useful for basic number validation but can be more efficient when used for SMS campaigns and marketing if in future versions these features are implemented as it would save alot of money as HLR validation does cost money and can filter out alot of non-valid numbers if the number strings generated were parsed through these filters before being HLR validated.

I have only tested this in an vscode IDE terminal, but with some tweaking of code you can make it nice and add licensing tools to it if you decide to sell Australian SMS leads.

![preview](https://user-images.githubusercontent.com/94292518/211355980-9234f173-b932-46a2-ba0b-eb3d08cca5aa.png)


