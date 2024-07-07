# SauceDemo Automation

This repository contains a Selenium script to automate interactions with the SauceDemo website. The script performs the following tasks:

1. Logs into the website with provided credentials.
2. Adds two items to the shopping cart.
3. Verifies that the items have been added.
4. Logs out of the website.

## Libraries Used

- `selenium` for browser automation.

## Requirements

- Python 3.x
- ChromeDriver (compatible with your version of Chrome)
- Selenium library

## Setup

1. Clone the repository.

    ```shell
    git clone https://github.com/your-repo/saucedemo-automation.git
    cd saucedemo-automation
    ```

2. Install the required Python packages.

    ```shell
    pip install selenium
    ```

3. Download and set up ChromeDriver.

    - Ensure you have [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) installed.
    - Update the `chrome_driver_path` in the script to the location of your `chromedriver` executable.

## Running the Script

To execute the script, run:

```shell
python saucedemo_automation.py
