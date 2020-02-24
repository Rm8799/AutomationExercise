OVERVIEW

Testing framework includes test cases written in python using Selenium modules, and I chose PyCharm as my IDE out of familiarity.  Instruc tions on installing each of these components is given in the README.md file in this github repository.

Test cases inluded in this project are:

- Account creation
- Log in
- Shopping cart
- Browsing the store’s main categories (Women, Dresses, T-shirts)


NEXT STEPS

1. Expanding the test suite to include the remaining test cases 
  - Checkout:
  Includes adding items to cart and validating each step of the checkout process: Summary, Sign In, Address, Shipping, Payment
  To validate the checkout process itself, I would recommend using as few items as possible.  Adding multiple items to the shopping       cart, and confirming the total $ could be written as a separate test.
  
  - Searching for clothing items:
  Recommended to break this is into multiple test cases that use search criteria that return results from varyious shopping categories,   as well as confirming that the search functionality properly returns individual or multiple items.
  
  - Sharing an item via social media:
  Individual test cases for each social media link on a single item (Twitter, Facebook, Google+, Pinterest)
  Since these sharing links redirect to external websites, those sites' functionaly needn't be tested here.  Recommend writing test       cases focused on just validating the website that each external link element is going to redirect the user to.
  
2. Expanding framework to include keyword driven test cases ,using a framework such as Robot, is highly recommended before expanding UI/end-to-end test suites.  This allows for test cases to be written in a much more compact manner that is also much easier to read for readers unfamiliar with Python or other languages, or just anyone new to the testing framework.  
  
