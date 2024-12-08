package main

import (
	"encoding/json"
	"github.com/buger/jsonparser"
	"os"
)

var _book_title string = ""
var _book_url string = ""
var _author_name string = ""
var _author_url string = ""
var _seria_name string = ""
var _seria_number string = ""
var _seria_url string = ""
var _chapters = []_chapter{}

type _chapter struct {
	Title   string `json:"title"`
	IsValid bool   `json:"valid"`
}

type Result struct {
	Book_title   string     `json:"book_title"`
	Book_url     string     `json:"book_url"`
	Author_name  string     `json:"author_name"`
	Author_url   string     `json:"author_url"`
	Seria_name   string     `json:"seria_name"`
	Seria_number string     `json:"seria_number"`
	Seria_url    string     `json:"seria_url"`
	Chapters     []_chapter `json:"chapters"`
}

func parseOne(key []byte, value []byte, dataType jsonparser.ValueType, offset int) error {

	_key := string(key)

	if _key == "Title" {
		_book_title, _ = jsonparser.ParseString(value)
	}
	if _key == "Url" {
		_book_url, _ = jsonparser.ParseString(value)
	}
	if _key == "Author" {
		_author_name, _ = jsonparser.GetString(value, "Name")
		_author_url, _ = jsonparser.GetString(value, "Url")
	}
	if _key == "Seria" {
		_seria_name, _ = jsonparser.GetString(value, "Name")
		_seria_number, _ = jsonparser.GetString(value, "Number")
		_seria_url, _ = jsonparser.GetString(value, "Url")
	}
	if _key == "Chapters" {
		jsonparser.ArrayEach(value, func(item []byte, itemDataType jsonparser.ValueType, itemOffset int, err error) {
			_Title, _ := jsonparser.GetString(item, "Title")
			_IsValid, _ := jsonparser.GetBoolean(item, "IsValid")

			chapter := _chapter{Title: _Title, IsValid: _IsValid}
			_chapters = append(_chapters, chapter)
		})
	}
	return nil
}

func main() {
	orig := os.Args[1]

	fileName := orig
	data, err := os.ReadFile(fileName)
	if err != nil {
		panic(err)
	}
	jsonparser.ObjectEach(data, parseOne)

	res := Result{Book_title: _book_title, Book_url: _book_url, Author_name: _author_name, Author_url: _author_url, Seria_name: _seria_name, Seria_number: _seria_number, Seria_url: _seria_url, Chapters: _chapters}

	file, err1 := json.Marshal(res)
	if err1 != nil {
		panic(err1)
	}

	err2 := os.WriteFile(orig, file, 0644)
	if err2 != nil {
		panic(err2)
	}
}
