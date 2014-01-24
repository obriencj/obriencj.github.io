MARKDOWN := $(patsubst %.md,%.html,$(wildcard *.md))

all: $(MARKDOWN)

%.html: %.md
	multimarkdown $< -o $@
	git add $< $@

