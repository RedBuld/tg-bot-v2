import ijson, orjson, asyncio, time

async def _test() -> None:

	_book_title = ''
	_book_url = ''
	_author_name = ''
	_author_url = ''
	_seria_name = ''
	_seria_number = ''
	_seria_url = ''
	_chapters = []
	_chapter = None
	with open("t2.json", "rb") as f:
		parser = ijson.parse(f)
		for prefix, event, value in parser:
			if prefix == 'Title':
				_book_title = value
			if prefix == 'Url':
				_book_url = value
			if prefix == 'Author.Name':
				_author_name = value
			if prefix == 'Author.Url':
				_author_url = value
			if prefix == 'Seria.Name':
				_seria_name = value
			if prefix == 'Seria.Number':
				_seria_number = value
			if prefix == 'Seria.Url':
				_seria_url = value
			if prefix == 'Chapters.item' and event == 'start_map':
				_chapter = {}
			if prefix == 'Chapters.item.Title':
				_chapter['Title'] = value
			if prefix == 'Chapters.item.IsValid':
				_chapter['IsValid'] = value
			if prefix == 'Chapters.item' and event == 'end_map':
				_chapters.append(_chapter)
				_chapter = None

	_json = orjson.dumps({
		"book_title":   _book_title,
		"book_url":     _book_url,
		"author_name":  _author_name,
		"author_url":   _author_url,
		"seria_name":   _seria_name,
		"seria_number": _seria_number,
		"seria_url":    _seria_url,
		"chapters":     _chapters,
	})

	with open("res_py.json", "wb") as f:
		f.write(_json)

start_time = time.time()
asyncio.run(_test())
elapsed = time.time() - start_time
print(f"Execution time: {elapsed}s")