import requests as req
import pandas as pd


# define main data
url = "https://exofop.ipac.caltech.edu/tess/target.php?id={starID}&json"
data = pd.read_excel("./data.xlsx")


# create fetcher
def fetchData(ID:int):
    print(f"fetch start data with ID: {ID}")
    response = req.get(url.format(starID=ID))
    return response.json()

tempData = {
    'basic_info': {'confirmed_planets': '',
                    'k2_campaign': '',
                    'star_names': 'TIC 270536913, 2MASS J21390612-3340438, APASS '
                                '17369533, Gaia DR2 6592175672898801024, HIP '
                                '106907, TYC 7490-00805-1, UCAC4 282-216684, '
                                'WISE J213906.16-334044.3',
                    'tic_contamination_ratio': 'none',
                    'tic_id': '270536913'},
    'coordinates': {'dec': '-33.679032609471101',
                    'ecliptic_lat': '-18.53328',
                    'ecliptic_long': '315.805',
                    'galactic_lat': '-48.3845',
                    'galactic_long': '11.74323',
                    'pm_dec': '-41.4492',
                    'pm_dec_error': '.0642107',
                    'pm_ra': '71.2392',
                    'pm_ra_error': '.0737244',
                    'ra': '324.77584915672901'},
    'ctois': [],
    'files': [],
    'imaging': [],
    'imaging_units': {'icont': '',
                    'idate': 'UT',
                    'ifilt': '',
                    'iinst': '',
                    'ipix': 'arcsec',
                    'ipsf': 'arcsec',
                    'itel': '',
                    'itype': ''},
    'magnitudes': [{'band': 'TESS',
                    'mdate': '2019-04-15',
                    'mgroup': '',
                    'mnotes': 'TIC v8.2',
                    'mtabname': 'tmag',
                    'mtag': '',
                    'muser': 'TESS project',
                    'value': '5.4616',
                    'value_e': '0.006'},
                    {'band': 'B',
                    'mdate': '2019-04-15',
                    'mgroup': '',
                    'mnotes': 'TIC v8.2',
                    'mtabname': 'bmag',
                    'mtag': '',
                    'muser': 'TESS project',
                    'value': '7.229',
                    'value_e': '0.019'},
                    {'band': 'V',
                    'mdate': '2019-04-15',
                    'mgroup': '',
                    'mnotes': 'TIC v8.2',
                    'mtabname': 'vmag',
                    'mtag': '',
                    'muser': 'TESS project',
                    'value': '6.28',
                    'value_e': '0.03'},
                    {'band': 'Gaia',
                    'mdate': '2019-04-15',
                    'mgroup': '',
                    'mnotes': 'TIC v8.2',
                    'mtabname': 'gaiamag',
                    'mtag': '',
                    'muser': 'TESS project',
                    'value': '6.02738',
                    'value_e': '0.000634747'},
                    {'band': 'J',
                    'mdate': '2019-04-15',
                    'mgroup': '',
                    'mnotes': 'TIC v8.2',
                    'mtabname': 'jmag',
                    'mtag': '',
                    'muser': 'TESS project',
                    'value': '4.923',
                    'value_e': '0.23'},
                    {'band': 'H',
                    'mdate': '2019-04-15',
                    'mgroup': '',
                    'mnotes': 'TIC v8.2',
                    'mtabname': 'hmag',
                    'mtag': '',
                    'muser': 'TESS project',
                    'value': '4.31',
                    'value_e': '0.192'},
                    {'band': 'K',
                    'mdate': '2019-04-15',
                    'mgroup': '',
                    'mnotes': 'TIC v8.2',
                    'mtabname': 'kmag',
                    'mtag': '',
                    'muser': 'TESS project',
                    'value': '4.251',
                    'value_e': '0.304'},
                    {'band': 'WISE 3.4 micron',
                    'mdate': '2019-04-15',
                    'mgroup': '',
                    'mnotes': 'TIC v8.2',
                    'mtabname': 'w1mag',
                    'mtag': '',
                    'muser': 'TESS project',
                    'value': '4.044',
                    'value_e': '0.277'},
                    {'band': 'WISE 4.6 micron',
                    'mdate': '2019-04-15',
                    'mgroup': '',
                    'mnotes': 'TIC v8.2',
                    'mtabname': 'w2mag',
                    'mtag': '',
                    'muser': 'TESS project',
                    'value': '3.825',
                    'value_e': '0.193'},
                    {'band': 'WISE 12 micron',
                    'mdate': '2019-04-15',
                    'mgroup': '',
                    'mnotes': 'TIC v8.2',
                    'mtabname': 'w3mag',
                    'mtag': '',
                    'muser': 'TESS project',
                    'value': '4.075',
                    'value_e': '0.016'},
                    {'band': 'WISE 22 micron',
                    'mdate': '2019-04-15',
                    'mgroup': '',
                    'mnotes': 'TIC v8.2',
                    'mtabname': 'w4mag',
                    'mtag': '',
                    'muser': 'TESS project',
                    'value': '4.043',
                    'value_e': '0.026'}],
    'planet_parameters': [],
    'planet_units': {'ar': '',
                    'arg': '',
                    'dens': 'g/cm^3',
                    'dep_m': 'mmag',
                    'dep_p': 'ppm',
                    'dur': 'hrs',
                    'ecc': '',
                    'epoch': 'BJD',
                    'eqt': 'K',
                    'imp': '',
                    'inc': 'deg',
                    'ins': 'Earth flux',
                    'mass': 'M_Earth',
                    'per': 'days',
                    'rad': 'R_Earth',
                    'rr': '',
                    'sma': 'AU',
                    'snr': '',
                    'time': 'BJD',
                    'vsa': 'm/s'},
    'spectroscopy': [],
    'spectroscopy_units': {'sapp': '',
                            'sdate': 'UT',
                            'sinst': '',
                            'ssnr1': '',
                            'ssnr2': '',
                            'ssres': 'R',
                            'stel': '',
                            'swave': ''},
    'stellar_companions': [],
    'stellar_companions_units': {'dmag': '',
                                'filt': '',
                                'odate': 'UT',
                                'pa': 'E of N (deg)',
                                'sep': 'arcsec'},
    'stellar_parameters': [{'prov': 'tic',
                            'prov_num': '1',
                            'prov_title': 'TESS Input Catalog Stellar Parameters'},
                            {'age': '',
                            'age_e': '',
                            'dens': '',
                            'dens_e': '',
                            'dist': '44.2836',
                            'dist_e': '0.1129',
                            'fitq': '',
                            'halpha': '',
                            'halpha_e': '',
                            'inst': '',
                            'logg': None,
                            'logg_e': None,
                            'logr': '',
                            'logr_e': '',
                            'lum': None,
                            'lum_e': None,
                            'mass': None,
                            'mass_e': None,
                            'met': None,
                            'met_e': None,
                            'otime': '',
                            'otime_e': '',
                            'rotper': '',
                            'rotper_e': '',
                            'rv': '',
                            'rv_e': '',
                            'sdate': '2019-04-15',
                            'sgroup': '',
                            'sindex': '',
                            'sindex_e': '',
                            'snotes': 'TIC v8.2',
                            'snr': '',
                            'snr_e': '',
                            'srad': '3.31831',
                            'srad_e': None,
                            'stag': '',
                            'suser': 'TESS project',
                            'teff': '5009',
                            'teff_e': '122',
                            'tel': '',
                            'vsini': '',
                            'vsini_e': ''}],
    'stellar_units': {'age': 'Gyr',
                    'dens': 'g/cm^3',
                    'dist': 'pc',
                    'halpha': '',
                    'logg': '',
                    'logr': '',
                    'lum': 'L_Sun',
                    'mass': 'M_Sun',
                    'met': '',
                    'otime': 'BJD',
                    'rotper': 'days',
                    'rv': 'm/s',
                    'sindex': '',
                    'snr': '',
                    'srad': 'R_Sun',
                    'teff': 'K',
                    'vsini': 'km/s'},
    'time_series': [],
    'time_series_units': {'tscam': '',
                        'tsdate': 'UT',
                        'tsdur': 'm',
                        'tsfilt': '',
                        'tsmag': '',
                        'tsnum': '',
                        'tspar': 'pixel',
                        'tspix': 'arcsec',
                        'tspsf': 'arcsec',
                        'tstcov': '',
                        'tstel': '',
                        'tstype': ''},
    'tois': []
}

def mergeData(index:int, newData:dict):

    lastData = list(data.iloc[index, :])
    stellar_parameters = newData['stellar_parameters'][1]

    lastData += [
        stellar_parameters['age'],
        stellar_parameters['age_e'],
        stellar_parameters['dist'],
        stellar_parameters['dist_e'],
        stellar_parameters['logg'],
        stellar_parameters['logg_e'],
        stellar_parameters['lum'],
        stellar_parameters['lum_e'],
        stellar_parameters['mass'],
        stellar_parameters['mass_e'],
        stellar_parameters['met'],
        stellar_parameters['met_e'],
        stellar_parameters['srad'],
        stellar_parameters['srad_e'],
        stellar_parameters['teff'],
        stellar_parameters['teff_e'],
    ]
    
    return lastData


# merged list
merged_list = []
result = None

# run for each data
for index, ID in enumerate(data['TIC ID']):
    tempData = fetchData(ID)
    merged_list.append(
        mergeData(index, tempData))

    result = pd.DataFrame(
        merged_list
    )
    result.to_excel("./result.xlsx")