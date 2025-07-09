FROM node:18-alpine AS inst
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

FROM node:18-alpine AS build
WORKDIR /app
COPY --from=inst /app/node_modules ./node_modules
COPY . .
RUN yarn build

FROM nginx:alpine AS production
COPY --from=build /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/frontend.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
