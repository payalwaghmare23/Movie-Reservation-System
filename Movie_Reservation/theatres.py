

theatres = {
    "Pune": [
        "PVR: Phoenix Market City, Pune", 
        "Cinepolis: Seasons Mall,Pune",
        "INOX Amanora" , 
        "City Pride: Kothrud",
        "Cinepolis: Westend Mall, Aundh"
        ],
   
    "Mumbai": [
        "PVR Juhu", 
        "INOX Marine" , 
        "Cinepolis: Nexus seawoods , nerul , Navi Mumbai" , 
        "BMX Cinemas Kharghar",
        "PVR: Phoenix Palladium, Lower Parel"
        ] ,

    "Delhi": [
        "PVR Select Citywalk",
        "INOX Nehru Place",
        "Cinepolis Saket",
        "Carnival Cinemas",
        "Wave Cinemas"
    ]
}


def get_theatre(city, index):
    city = city.title()
    
    theatre_list = theatres.get(city, [])
    
    if not theatre_list:
        return "No theatre available"
    
    return theatre_list[index % len(theatre_list)]