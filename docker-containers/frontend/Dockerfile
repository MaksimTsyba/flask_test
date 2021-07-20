FROM node:14.17.0-alpine3.12

RUN apk update && apk add bash
ENV APP /app
COPY frontend /app
WORKDIR $APP

CMD ["npm", "start"]