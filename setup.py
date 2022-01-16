import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='lightwave',
    version='0.20',
    description='Python library to provide a reliable communication link with LightWaveRF lights, switches and TRVs.',
    url='https://github.com/GeoffAtHome/lightwave',
    author='Geoff Soord',
    author_email='geoff@soord.org.uk',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=setuptools.find_packages(),
    keywords=['Lightwave', 'LightwaveRF',
              'Lightwave WiFiLink', 'Lightwave Link'],
    zip_safe=False
)
