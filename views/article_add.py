import flet as ft
import flet_easy as fs

from sqlmodel import  Session
from db import db

from models import ArticleBase, ArticleType, FragmentBase

article_add_page = fs.AddPagesy(
    route_prefix='/article'
)

@article_add_page.page(route='/add', title='Add Article')
def article_add(data: fs.Datasy):
    page = data.page
    session = Session(db.engine)

    def create_article(e):
        title_text = title.value
        content_text = content.value

        article = ArticleBase(
            name=title_text,
            article_type=ArticleType.Plain,
            text=content_text
        )

        article_db = db.save_article(article, session)

        fragments = []
        for fragment in article.fragmentize():
            fragments.append(FragmentBase(text=fragment))

        db.save_fragments(article_db, fragments, session)
        data.go_back()

    appbar = ft.AppBar(
        leading=ft.IconButton(
            ft.Icons.ARROW_BACK,
            icon_size=30,
            on_click=data.go_back()
        ),
        leading_width=40,
        title=ft.Text("Добавьте новый текст"),
        center_title=False,
        bgcolor=ft.Colors.BLUE_200,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Простой текст"),
                    ft.PopupMenuItem(text="PDF файл"),
                ]
            ),
        ],
    )

    cl = ft.Column(
        expand=True
    )
    title = ft.TextField(
            hint_text='Название',
            max_lines=1,
            text_size=14
        )
    cl.controls.append(title)

    content = ft.TextField(
            hint_text='Текст',
            max_lines=30,
            text_size=14,
            expand=True,
        )
    cl.controls.append(content)

    cl.controls.append(
        ft.TextButton(
            text='Сохранить',
            on_click=create_article
        )
    )

    return ft.View(
        controls=[
            cl
        ],
        appbar=appbar,
    )


# page.appbar = ft.AppBar(
#         leading=ft.Icon(ft.Icons.PALETTE),
#         leading_width=40,
#         title=ft.Text("AppBar Example"),
#         center_title=False,
#         bgcolor=ft.Colors.SURFACE_VARIANT,
#         actions=[
#             ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED),
#             ft.IconButton(ft.Icons.FILTER_3),
#             ft.PopupMenuButton(
#                 items=[
#                     ft.PopupMenuItem(text="Item 1"),
#                     ft.PopupMenuItem(),  # divider
#                     ft.PopupMenuItem(
#                         text="Checked item", checked=False, on_click=check_item_clicked
#                     ),
#                 ]
#             ),
#         ],
#     )


"""
///File download from FlutterViz- Drag and drop a tools. For more details visit https://flutterviz.io/

import 'package:flutter/material.dart';

class Add extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Color(0xffffffff),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisSize: MainAxisSize.max,
          children: [
            TextField(
              controller: TextEditingController(),
              obscureText: false,
              textAlign: TextAlign.start,
              maxLines: 1,
              style: TextStyle(
                fontWeight: FontWeight.w400,
                fontStyle: FontStyle.normal,
                fontSize: 14,
                color: Color(0xff000000),
              ),
              decoration: InputDecoration(
                disabledBorder: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(4.0),
                  borderSide: BorderSide(color: Color(0xff000000), width: 1),
                ),
                focusedBorder: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(4.0),
                  borderSide: BorderSide(color: Color(0xff000000), width: 1),
                ),
                enabledBorder: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(4.0),
                  borderSide: BorderSide(color: Color(0xff000000), width: 1),
                ),
                hintText: "Enter Text",
                hintStyle: TextStyle(
                  fontWeight: FontWeight.w400,
                  fontStyle: FontStyle.normal,
                  fontSize: 14,
                  color: Color(0xff000000),
                ),
                filled: true,
                fillColor: Color(0xfff2f2f3),
                isDense: false,
                contentPadding:
                    EdgeInsets.symmetric(vertical: 8, horizontal: 12),
              ),
            ),
            Expanded(
              flex: 1,
              child: TextField(
                controller: TextEditingController(),
                obscureText: false,
                textAlign: TextAlign.start,
                maxLines: 40,
                style: TextStyle(
                  fontWeight: FontWeight.w400,
                  fontStyle: FontStyle.normal,
                  fontSize: 14,
                  color: Color(0xff000000),
                ),
                decoration: InputDecoration(
                  disabledBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(4.0),
                    borderSide: BorderSide(color: Color(0xff000000), width: 1),
                  ),
                  focusedBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(4.0),
                    borderSide: BorderSide(color: Color(0xff000000), width: 1),
                  ),
                  enabledBorder: OutlineInputBorder(
                    borderRadius: BorderRadius.circular(4.0),
                    borderSide: BorderSide(color: Color(0xff000000), width: 1),
                  ),
                  hintText: "Enter Text",
                  hintStyle: TextStyle(
                    fontWeight: FontWeight.w400,
                    fontStyle: FontStyle.normal,
                    fontSize: 14,
                    color: Color(0xff000000),
                  ),
                  filled: true,
                  fillColor: Color(0xfff2f2f3),
                  isDense: false,
                  contentPadding:
                      EdgeInsets.symmetric(vertical: 8, horizontal: 12),
                ),
              ),
            ),
            Padding(
              padding: EdgeInsets.symmetric(vertical: 10, horizontal: 0),
              child: MaterialButton(
                onPressed: () {},
                color: Color(0xffffffff),
                elevation: 0,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.zero,
                  side: BorderSide(color: Color(0xff808080), width: 1),
                ),
                padding: EdgeInsets.all(16),
                child: Text(
                  "Button",
                  style: TextStyle(
                    fontSize: 14,
                    fontWeight: FontWeight.w400,
                    fontStyle: FontStyle.normal,
                  ),
                ),
                textColor: Color(0xff000000),
                height: 40,
                minWidth: 140,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

"""