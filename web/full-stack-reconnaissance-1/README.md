# Title 
Full-Stack-Reconnaissance

# Author
Kaled Aljebur

# Description:
Participants begin by examining the available frontend interface to 
gather initial information and identify accessible routes. Using browser developer tools and basic web inspection techniques, they observe how the frontend communicates with a separate backend service, potentially hosted on a different port.
By analysing network requests and application behaviour, participants can enumerate backend endpoints, compare frontend and backend responses, and identify inconsistencies or exposed data. Through careful observation rather than brute-force, they uncover hidden information such as sensitive API paths or unfiltered backend content, ultimately leading to flag discovery.

# Complexity level
- Intro to intermediate level, but can be complicated for future CTF competitions if needed.

# Key Learning Objectives & Challenges:
1. Understanding Web Application Architecture: Participants will recognise that the frontend (served on one port, e.g., 3000) and the backend API (served on a different port, e.g., 7123) are separate components. Identifying and understanding this separation is essential to navigating and exploiting the application correctly.
1. Targeted Port Discovery Techniques: The backend service listens on a non-standard port (e.g., 7123) that may not be included in default scanning tools like Nmap. Participants must use options such as -p 7123 or -p- to discover the backend service explicitly.
1. Proficiency with Developer Tools and Traffic Inspection: Participants are expected to use browser developer tools (such as Chrome DevTools) or tools like Wireshark to analyze frontend network requests. This will reveal the backend API endpoints, request parameters, and responses—critical for locating and understanding the flags.

# Reconnaissance and enumeration steps
- Participants begin by identifying open ports and the services running on them. Recognising the separation between frontend and backend is key.
- They are expected to assess what parts of the application are exposed and might lead to vulnerabilities though there are no input fields or URL parameters in the frontend, so injection-based attacks are not applicable.
- Through exploration, participants should realise they are working with a full-stack application, meaning both the frontend (React) and backend (Flask) must be analysed separately.
- The frontend JavaScript bundle (a compact/minified file) may contain clues to hidden routes or hardcoded API endpoints. Reviewing this file is essential for identifying potential access points.
- Logical reasoning should lead participants to enumerate possible hidden URLs or routes on both the frontend and backend.
- Frontend Route Enumeration:
    - There are approximately eight frontend routes.
    - These can be found by:
        - Manually exploring the application,
        - Reviewing the frontend JS code,
        - Using browser developer tools.
    - Flag 1 is located in one of these frontend routes.
- Backend Route Enumeration
    - Similarly, there are around eight backend routes.
    - These must be tested manually by crafting requests directly to the backend service (once its port is identified).
    - Flag 2 is located at the root of the backend endpoint (e.g., http://domain.com:backend_port/).
- Analysing Frontend-Backend Interactions
    - Participants will observe that the frontend calls backend endpoints using different query parameters.
    - To uncover Flag 3, they must test these backend endpoints both:
        - With query parameters (e.g., ?filtered=true)
        - And without any query parameters.
    - Careful comparison of the backend responses will reveal the flag is only exposed when no parameters are provided, showcasing a frontend-backend filtering mismatch.

# Tools
- Browser Developer Tools
- cURL or HTTPie
- Nmap
- Burp Suite and HTTPie 
- Wireshark
- wget and js-beautify 

# Flags' locations:
1. The first flag is in `http://domain.com:3000/info`
1. The second flag is in `http://domain.com:7123`
1. The third flag is in `http://domain.com:7123/client`

# Flags
- `pecan{flag1_!shfHUkf^32Gaf*/}`
- `pecan{flag2_sf@hNsa;*67^$4fJ}`
- `pecan{flag3_a#GkjJHY743$$9JF}`