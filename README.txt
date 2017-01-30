Build Instructions:  

No need to build, application is built and running at https://still-meadow-35970.herokuapp.com.
Inventory by product can be seen at https://still-meadow-35970.herokuapp.com/inventorybyproduct.

Approach/Potential Improvements:

Tools: 
I feel most comfortable developing in python, and flask is a good framework to use for quick POCs such as this one. If I were to make this into a larger/full blown application, I might want to switch over to Django or consider using other tools entirely such as Ruby on Rails.

Design: 
Model was taken directly from spreadsheets. One nuance that probably makes sense to fix is making product_id the id field of Product.

Loading db was pretty straightforward, although I could potentially reference columns by name instead of position to make it more robust.  

In terms of API, I had initially started building several more routes. One was similar to the one I implemented but to see product/inventory for only one product (could make controller more generic to handle both of these cases).  I also had added a bit of error handling there, to display 404 if trying to get a product that doesn't exist.  Other proposed routes had to do with filtering by inventory fields - ie. show me only products/related inventory for 'jet blue' style products.  This could be implemented by passing a json with all search criteria and doing a query filter on all of these. 

Additionally, I'm not sure if my route/corresponding html are properly named. I know these routes should usually correspond to resources.  As such, I originally had this route as /product, but since it returns a combination of product and inventory information, I decided to name it more explicitly.  

Another improvement I could make is creating a better separation between controller logic and json/util stuff - ie. could have queried product/inventory first and then passed to util to create json instead of doing Inventory query in that function.  

Lastly, I could always add some unit tests to ensure db is loaded properly and api calls work as expected.



