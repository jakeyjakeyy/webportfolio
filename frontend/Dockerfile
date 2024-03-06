# build
FROM node:lts-alpine
WORKDIR /app/frontend
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/frontend/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]