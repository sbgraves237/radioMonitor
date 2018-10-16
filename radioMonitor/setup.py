from distutils.core import setup
import setuptools

setup(
    name='radioMonitor1',
    version='0.1dev',
    author = "Spencer Graves", 
    author_email = "spencer.graves@effectivedefense.org", 
    description = "Read audio in > a series of wav files", 
    url = "https://github.com/sbgraves237/radioMonitor"
    packages=setuptools.find_packages(),
#    packages=['radioMonitor',],
    license='CC BY-NC-SA'
#   Spencer Graves and others who 
#   contribute to this code with volunteer labor.
#   This allows nonprofits to use it for free 
#   without limiting our ability to 
#   negotiate for royalties from 
#   commercialization by a for-profit company.  
#   If that doesn't happen, we may later release it 
#   under the more standard GNU GPL:  
#    license='GNU General Public License',
#    long_description=open('README.txt').read(),
)
