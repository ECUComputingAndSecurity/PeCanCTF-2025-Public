# --------- build image ----------
FROM nginx:alpine

# Copy Nginx config first (so edits cause cache bust)
COPY nginx.conf /etc/nginx/nginx.conf

# Copy static assets
COPY public-site   /usr/share/nginx/html/public-site
COPY internal-site /usr/share/nginx/html/internal-site
COPY common        /usr/share/nginx/html/common

# Expose challenge port
EXPOSE 8080

# Run nginx in foreground
CMD ["nginx", "-g", "daemon off;"]
