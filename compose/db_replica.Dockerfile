FROM postgres:12.1-alpine

ENV GOSU_VERSION 1.10

RUN apk add --update iputils

COPY ./compose/db/slave-entrypoint.sh /slave-entrypoint.sh
RUN chmod +x /slave-entrypoint.sh

ADD ./compose/db/gosu /usr/bin/
RUN chmod +x /usr/bin/gosu

ENTRYPOINT [ "/slave-entrypoint.sh" ]

CMD ["gosu", "postgres", "postgres"]
