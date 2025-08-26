In this challenge, students will leverage geospatial OSINT tools like [Overpass Turbo](https://overpass-turbo.eu/) to uncover the location of Parkdale Secondary College. This school is uniquely positioned as the closest high school to an airport in Melbourne’s southern suburbs, making it a key piece of the puzzle. Additionally, Parkdale Secondary College is bordered by a golf course — another clue to help guide participants toward the correct school.

The challenge encourages students to build a smart query using Overpass Turbo to search for schools located near both airports and golf courses. While using Overpass Turbo is the most efficient method, students can also take a more manual approach by examining nearby airports and high schools using tools like Google Maps. Both methods are acceptable, but utilizing the tool is the preferred and intended route for solving this challenge.

The goal is to get students familiar with geospatial OSINT tools while also fostering problem-solving skills through creative use of data.

Some example Overpass Turbo queries:

```
[out:json][timeout:25];
(
	nwr["leisure"="golf_course"]({{bbox}});
  	nwr["aeroway"="aerodrome"]({{bbox}});
	nwr["amenity"="school"]({{bbox}});
);
out geom;
```

```
[out:json][timeout:60];

// Step 1: Find schools with "High" or "Secondary" in the name
(
  node["amenity"="school"]["name"~"(High|Secondary)",i]( -38.433, 144.272, -37.460, 145.520 );
  way["amenity"="school"]["name"~"(High|Secondary)",i]( -38.433, 144.272, -37.460, 145.520 );
  relation["amenity"="school"]["name"~"(High|Secondary)",i]( -38.433, 144.272, -37.460, 145.520 );
)->.schools;

// Step 2: Find airports in Melbourne
(
  node["aeroway"="aerodrome"]( -38.433, 144.272, -37.460, 145.520 );
  way["aeroway"="aerodrome"]( -38.433, 144.272, -37.460, 145.520 );
  relation["aeroway"="aerodrome"]( -38.433, 144.272, -37.460, 145.520 );
)->.airports;

// Step 3: Find golf courses
(
  node["leisure"="golf_course"]( -38.433, 144.272, -37.460, 145.520 );
  way["leisure"="golf_course"]( -38.433, 144.272, -37.460, 145.520 );
  relation["leisure"="golf_course"]( -38.433, 144.272, -37.460, 145.520 );
)->.golfcourses;

// Step 4: Filter schools that are near airports and golf courses
(
  node.schools(around.airports:5000)(around.golfcourses:1000);
  way.schools(around.airports:5000)(around.golfcourses:1000);
  relation.schools(around.airports:5000)(around.golfcourses:1000);
);
out center;
```
