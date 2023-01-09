# au_leads
 
This python script allows the user to specify how many phone numbers they want to generate, generates those phone numbers without duplicates, saves those phone numbers to a .txt file, and gives the option to perform HLR validation on those numbers using the NumVerify API, and displays the carrier and validity information for each number in the text file. 

It then saves the validated phone numbers, along with the carrier and validity information, to the specified file and outputs a message indicating that the validated phone numbers were saved.  

Note that in order for this program to work, you will need to sign up for an API key from NumVerify. Replace API_KEY in the program with your own API key.

To do:
I was thinking of implementing a WhatsApp Filter and Facebook Filter to further validate numbers and filter out inactive ones as HLR validation can only provide if a mobile number has been registered, and may still be inactive. Nevertheless, useful for basic number validation but can be more efficient if in future versions these features are implemented as it would save alot of money as HLR validation does cost money and can filter out alot of non-valid numbers if the number strings generated were parsed through these filters before being HLR validated.
