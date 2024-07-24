# Find the URI of our newly created file
>>> uri = file_uri("counter.html")

# Use the URI to open the web page
>>> driver.get(uri)

# Access the title of the current page
>>> driver.title
'Counter'

# Access the source code of the page
>>> driver.page_source
'<html lang="en"><head>\n        <title>Counter</title>\n        <script>\n            \n            // Wait for page to load\n            document.addEventListener(\'DOMContentLoaded\', () => {\n\n                // Initialize variable to 0\n                let counter = 0;\n\n                // If increase button clicked, increase counter and change inner html\n                document.querySelector(\'#increase\').onclick = () => {\n                    counter ++;\n                    document.querySelector(\'h1\').innerHTML = counter;\n                }\n\n                // If decrease button clicked, decrease counter and change inner html\n                document.querySelector(\'#decrease\').onclick = () => {\n                    counter --;\n                    document.querySelector(\'h1\').innerHTML = counter;\n                }\n            })\n        </script>\n    </head>\n    <body>\n        <h1>0</h1>\n        <button id="increase">+</button>\n        <button id="decrease">-</button>\n    \n</body></html>'

# Find and store the increase and decrease buttons:
driver.find_element(By.ID,"increase")

>>> increase = driver.find_element(By.ID,"increase")
>>> decrease = driver.find_element(By.ID,"decrease")

# Simulate the user clicking on the two buttons
>>> increase.click()
>>> increase.click()
>>> decrease.click()

# We can even include clicks within other Python constructs:
>>> for i in range(25):
...     increase.click()