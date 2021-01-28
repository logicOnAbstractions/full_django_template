FROM nginx:1.19.6

# getting ride of nginx default stuff, replacing with our own
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d