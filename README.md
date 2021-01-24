# Lyrics Crawler
Crawls lyrics from KKBOX and MOJIM

## Goal
From list of albums and corresponding artists, find the song names and lyrics in the album.

## Sub-tasks
- [x] 1. read data, get album name and artist name.
- [x] 2. search on KKBOX/MOJIM for the album; For each result, return album name, artist name, and album link.
- [x] 3. check which result is needed by returned album name and artist name.
- [x] 4. from the album link, crawl the song names (and links) in the album.
- [x] 5. from the song link, crawl the lyrics of the song, store the lyrics as files.
- [ ] 6. compute the language proportion in each lyrics file.
- [ ] 7. fill the album-artist-song(-language) csv

## References
1. `requests`: https://blog.gtwang.org/programming/python-requests-module-tutorial/
2. `beautifulsoup`: https://blog.gtwang.org/programming/python-beautiful-soup-module-scrape-web-pages-tutorial/
3. find element by class: https://stackoverflow.com/questions/5041008/how-to-find-elements-by-class
4. save a file with `'/'` in name (conclusion: there's no way to achieve this): https://stackoverflow.com/questions/55390630/how-save-a-file-in-python-whose-name-has-slashes-in-it
5. split string with multiple delimiters (conclusion: use regex): https://stackoverflow.com/questions/4998629/split-string-with-multiple-delimiters-in-python
6. `re`: https://docs.python.org/3/library/re.html
7. `os.path`: https://docs.python.org/3/library/os.path.html
8. how to check if a file exists: https://linuxize.com/post/python-check-if-file-exists/
9. `csv`: https://docs.python.org/3/library/csv.html
10. "with open" multiple files in one line: https://stackoverflow.com/questions/4617034/how-can-i-open-multiple-files-using-with-open-in-python
11. convert `<br>` to `\n`: https://stackoverflow.com/questions/12545897/convert-br-to-end-line
12. raising exceptions: https://docs.python.org/3/tutorial/errors.html#raising-exceptions
