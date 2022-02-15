from bs4 import BeautifulSoup
import time
from pip import main
import requests
import pandas as pd
import urllib3
from datetime import datetime
from random import randrange

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


header = {"Connection": "keep-alive",
"Cache-Control": "max-age=0",
"sec-ch-ua": "\" Not;A Brand\";v=\"99\", \"Google Chrome\";v=\"97\", \"Chromium\";v=\"97\"",
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "\"Windows\"",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Sec-Fetch-Site": "none",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-User": "?1",
"Sec-Fetch-Dest": "document",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
"Cookie": "csrf=EB3C38F8-8E34-11EC-B03F-D6EAC25052B6--d471f697e3afad23e1e03ff4bd2787e5af34dc6e; _pk_id.3.7fcc=8abbd2132441835e.1644309686.; OptanonAlertBoxClosed=2022-02-08T08:42:35.474Z; OTAdditionalConsentString=1~39.43.46.55.61.66.70.83.89.93.108.117.122.124.131.135.136.143.144.147.149.159.162.167.171.192.196.202.211.218.228.230.239.241.259.266.272.286.291.311.317.322.323.326.327.338.367.371.385.389.394.397.407.413.415.424.430.436.440.445.449.453.482.486.491.494.495.501.503.505.522.523.540.550.559.560.568.574.576.584.587.591.733.737.745.780.787.802.803.817.820.821.829.839.864.867.874.899.904.922.931.938.979.981.985.1003.1024.1027.1031.1033.1034.1040.1046.1051.1053.1067.1085.1092.1095.1097.1099.1107.1127.1135.1143.1149.1152.1162.1166.1186.1188.1201.1205.1211.1215.1226.1227.1230.1252.1268.1270.1276.1284.1286.1290.1301.1307.1312.1345.1356.1364.1365.1375.1403.1415.1416.1419.1440.1442.1449.1455.1456.1465.1495.1512.1516.1525.1540.1548.1555.1558.1564.1570.1577.1579.1583.1584.1591.1603.1616.1638.1651.1653.1665.1667.1677.1678.1682.1697.1699.1703.1712.1716.1721.1722.1725.1732.1745.1750.1765.1769.1782.1786.1800.1808.1810.1825.1827.1832.1837.1838.1840.1842.1843.1845.1859.1866.1870.1878.1880.1889.1899.1917.1929.1942.1944.1962.1963.1964.1967.1968.1969.1978.2003.2007.2008.2027.2035.2039.2044.2046.2047.2052.2056.2064.2068.2070.2072.2074.2088.2090.2103.2107.2109.2115.2124.2130.2133.2137.2140.2145.2147.2150.2156.2166.2177.2183.2186.2202.2205.2216.2219.2220.2222.2225.2234.2253.2264.2279.2282.2292.2299.2305.2309.2312.2316.2322.2325.2328.2331.2334.2335.2336.2337.2343.2354.2357.2358.2359.2366.2370.2376.2377.2387.2392.2394.2400.2403.2405.2407.2411.2414.2416.2418.2425.2427.2440.2447.2459.2461.2462.2465.2468.2472.2477.2481.2484.2486.2488.2492.2493.2496.2497.2498.2499.2501.2510.2511.2517.2526.2527.2532.2534.2535.2542.2544.2552.2563.2564.2567.2568.2569.2571.2572.2575.2577.2583.2584.2589.2595.2596.2601.2604.2605.2608.2609.2610.2612.2614.2621.2628.2629.2633.2634.2636.2642.2643.2645.2646.2647.2650.2651.2652.2656.2657.2658.2660.2661.2669.2670.2677.2681.2684.2686.2687.2690.2695.2698.2707.2713.2714.2729.2739.2767.2768.2770.2772.2784.2787.2791.2792.2798.2801.2805.2812.2813.2816.2817.2818.2821.2822.2827.2830.2831.2834.2836.2838.2839.2840.2844.2846.2847.2849.2850.2851.2852.2854.2856.2860.2862.2863.2865.2867.2869.2873.2874.2875.2876.2878.2879.2880.2881.2882.2883.2884.2886.2887.2888.2889.2891.2893.2894.2895.2897.2898.2900.2901.2908.2909.2911.2912.2913.2914.2916.2917.2918.2919.2920.2922.2923.2924.2927.2929.2930.2931.2939.2940.2941.2942.2947.2949.2950.2956.2961.2962.2963.2964.2965.2966.2968.2970.2973.2974.2975.2979.2980.2981.2983.2985.2986.2987.2991.2993.2994.2995.2997.2999.3000.3002.3003.3005.3008.3009.3010.3012.3016.3017.3018.3019.3024.3025.3028.3034.3037.3038.3043.3044.3045.3048.3052.3053.3055.3058.3059.3063.3065.3066.3068.3070.3072.3073.3074.3075.3076.3077.3078.3089.3090.3093.3094.3095.3097.3099.3100.3104.3106.3109.3111.3112.3116.3117.3118.3119.3120.3124.3126.3127.3128.3130.3135.3136.3145.3149.3150.3151.3154.3155.3162.3163.3167.3172.3173.3180.3182.3183.3184.3185.3187.3188.3189.3190.3194.3196.3197.3209.3210.3211.3214.3215.3217.3219.3222.3223.3225.3226.3227.3228.3230.3231.3232.3234.3235.3236.3237.3238.3240.3241.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.3281.3288.3290.3292.3293.3295.3296; iom_consent=010fff0fff&1644309755711; _gbc=75b29ed5bbff45d5a63c8156ab095981; gb_has_push_support=1; gb_push_permission=default; gb_is_push_subscriber=0; __gads=ID=9de3f6997a5ee0c6:T=1644309756:S=ALNI_MaPmRUa2i1W8DvIQPmJMc7e_T4VqQ; GeizhalsConfcookie=darkmode&off&hloc:default&at"}

# Scrape TOP 10 cheapest offers for url 


products = pd.read_csv(r'C:\Users\THOMSENG\Desktop\lets py around\ordercode2id_clean.csv', sep=';')
list = list(products["GH_id"])
#print(len(list))

#define Datafram
df = pd.DataFrame(columns=["GH_id", "Platz", "Anbieter", "Preis", "URL","Datetime"])

counter = 0
for i in list:
    counter+=1
    url = 'https://geizhals.de/'+str(i)
    req = requests.get(url, verify=False, headers=header)
    soup = BeautifulSoup(req.content, 'html.parser')

    #catch den Banhammer

    #Searching TOP 10 Offers
    ranger = range(0,10)
    numberProd = 0
    for l in ranger:
        numberProd+=1
        #Get Offer
        offer_id = "offer__" + str(l)
        li = soup.find('div', {'id': offer_id})
        if li is None: 
             
            break

        #Get Name
        merch = li.find('span',{'class': 'merchant__logo-caption'})
        name = merch.find('span',{'class': 'notrans'}).string.strip()

        #Get Price
        price = li.find('div',{'class': 'offer__price'})
        pricer = price.find('span',{'class': 'gh_price'}).string.replace('€ ', '')

        #Get Link
        liver = li.find('div', {'class': 'cell offer__merchant'})
        redirectURL = liver.find('a').get('href')
        finalURL = "https://www.geizhals.de"+redirectURL

        #print(l+1,name, pricer, finalURL)
        #Get Time
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")


        #fill data into df
        newRow = pd.DataFrame(
                {
                  "GH_id": [i],
                  "Platz": [l+1],
                  "Anbieter": [name],
                  "Preis": [pricer],
                  "URL": [finalURL],
                  "Datetime": [dt_string]
                })

        frame = [df, newRow]
        df = pd.concat(frame, ignore_index=True)

    #print(str(i), numberProd)
    if counter%10 ==0:
        print(counter)
    #random = randrange(3)       
    #time.sleep(random)


#export dataframe
#df.to_csv('scrapedPricerrr.csv')

#df mergen: GH_id --> Ordercodes & Ordercode --> Product Infos, HEK
#bei Preis das € wegnehmen für Zahlenwerte
#eigene Spalte [HEK CHECK], HEK MARGIN, HEK DIFF

products_input = pd.read_csv(r'C:\Users\THOMSENG\Desktop\lets py around\products.csv', sep=';')

df1 = pd.merge(df, products, on='GH_id',how='left')
df2 = pd.merge(df1, products_input, left_on='Ordercode', right_on='Material', how='left')
df2.drop(columns=['Material', 'Bezeichnung'])

now = datetime.now()
dt_string = now.strftime("%d%m%Y_%H%M")
df_name = 'online_prices' + dt_string + '.csv'
df2.to_csv(df_name)