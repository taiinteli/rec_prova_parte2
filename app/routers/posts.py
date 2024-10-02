from fastapi import APIRouter, HTTPException, status
from models.blog_posts import BlogPost
from app.models.vars import BlogPostRequest, BlogPostUpdateRequest


from typing import List

import logging

LOGGER = logging.getLogger(__name__)

blog_posts = []

router = APIRouter(tags=['blog'])

class BlogPost:
    def __init__(id, self, usuario, review, serie_filme, estrelas):
        self.id = '1'
        self.usuario = 'nome_usuario'
        self.review = 'este filme foi supimpa'
        self.serie_filme = 'pokemon a vingança de mewteo'
        self.estrelas = '5'

    def __str__(self) -> str:
        return f'{self.id} - {self.usuario} - {self.review} - {self.serie_filme} - {self.estrelas}'
    
    def toJson(self):
        return {'id': self.id, 'usuario': self.usuario, 'review': self.review, 'serie_filme': self.serie.filme, 'estrelas': self.estrelas}


@router.post("/")
def create_blog_post(blog_post: BlogPostRequest, status_code=status.HTTP_201_CREATED):
    LOGGER.info({'message':'novo', 'post':blog_post, 'status':'success', 'method':'POST', 'url':'/blog'})
    try: 
        post = BlogPost(id=blog_post.id, usuario=blog_post.usuario, review=blog_post.review, serie_filme=blog_post.serie_filme, estrelas=blog_post.estrelas)
        blog_posts.append(post)
        return {'status':'success'}
    
    
@router.get("/")
def get_blog_posts():
    LOGGER.info({'message':'reviews', 'status':'success', 'method':'GET', 'url':'/blog'})
    LOGGER.debug(msg=f'Posts: {blog_posts}')
    return [post.toJson() for post in blog_posts]

@router.get("/{id}")
def get_blog_post(id: int):
    LOGGER.info({'message':'reviews/id', 'id':id, 'status':'success', 'method':'GET', 'url':'/blog'})
    for post in blog_posts:
        if post.id == id:
            return post.toJson()
    LOGGER.warning({'message':'Post not found', 'id':id, 'status':'error', 'method':'GET', 'url':'/blog'})
    raise HTTPException(status_code=404, detail='Post not found')


