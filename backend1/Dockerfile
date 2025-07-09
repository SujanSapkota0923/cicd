FROM node:18-alpine AS inst
WORKDIR /app
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile

FROM node:18-alpine
WORKDIR /app
COPY --from=inst /app/node_modules ./node_modules
COPY . .
CMD ["sh","yarn.sh"]

