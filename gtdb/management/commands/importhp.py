from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import User
from gtdb.models import Entity, Game, News, Comment, Review, URLlink
import json
from django.db import transaction
import sys

#IMP_DATE = '2013-04-01T00:00:00+00:00'

def iter_fields_and_do(Clazz, field_name, func):
    for field in Clazz._meta.local_fields:
        if field.name == field_name:
            func(field)
def turn_off_auto_now(Clazz, field_name):
    def auto_now_off(field):
        field.auto_now = False
    iter_fields_and_do(Clazz, field_name, auto_now_off)

def turn_off_auto_now_add(Clazz, field_name):
    def auto_now_add_off(field):
        field.auto_now_add = False
    iter_fields_and_do(Clazz, field_name, auto_now_add_off)

def sub_comments(game,parent,dic):
    for l in dic:
        com = Comment.objects.create(
            created_date = l['timestamp'],
            updated_date = l['timestamp'],
            description = l['comment'],
            entity = parent,
            title = l['subject'],
            reporter = l['user'],
            #parent = parent
        )
        sub_comments(game, com, l['comments'])        

#User.objects.get_or_create(username=username)

class Command(BaseCommand):
    help = 'Imports the de-normalised happypuppy data'

    def handle(self, *args, **options):
        # Disable auto transactions - increase import performance
        transaction.enter_transaction_management(managed=True)
        transaction.managed(flag=True)
        count = 0

        # Hack to let us set auto-dates manualy for import
        turn_off_auto_now(Entity, 'updated_date')
        turn_off_auto_now_add(Entity, 'created_date')
        '''turn_off_auto_now(Game, 'updated_date')
        turn_off_auto_now_add(Game, 'created_date')
        turn_off_auto_now(News, 'updated_date')
        turn_off_auto_now_add(News, 'created_date')
        turn_off_auto_now(Comment, 'updated_date')
        turn_off_auto_now_add(Comment, 'created_date')'''
        
        doc = json.load(open('%s/data/games.json' % (settings.PROJECT_ROOT)))
        for g in doc[:200]:
            #print(json.dumps(g,indent=4,sort_keys=True))
            
            # Not handling: screenshot, other, approved_by, approved_date, author, company
            
            game = Game.objects.create(
                title=g['title'],
                description=g['description'],
                short=g['short_description'],
                reporter=g['submitted_by'],
                created_date = '%sT00:00:00+00:00' % (g['date_sumbitted']),
                updated_date = g['timestamp'] if g['timestamp'] else '%sT00:00:00+00:00' % (g['date_sumbitted']),
                cost = g['cost'],
                version = g['version'],
            )
            for c in g['capabilities']:
                game.tags.add('cap:%s' % (c))
            game.tags.add('lic:%s' % (g['license']))
            
            for l in g['comments']:
                com = Comment.objects.create(
                    created_date = l['timestamp'],
                    updated_date = l['timestamp'],
                    description = l['comment'],
                    entity = game,
                    title = l['subject'],
                    reporter = l['user']
                )
                sub_comments(game, com, l['comments'])
        
            for r in g['ratings']:
                rate = Review.objects.create(
                    created_date = l['timestamp'],
                    updated_date = l['timestamp'],
                    entity=game,
                    title=g['title'],
                    reporter=r['user'],
                    score=r['rating']
                )
            for u in g['urls']:
                URLlink.objects.create(
                    entity=game,
                    desc=u['description'] if u['description'] else 'unnamed',
                    url=u['url']
                )
            if g['homepage']:
                URLlink.objects.create(
                    entity=game,
                    desc='homepage',
                    url=g['homepage']
                )
                        
            count = count+1
            if count==100:
                sys.stdout.write('.')
                sys.stdout.flush()
                count=0
                transaction.commit()
                
        doc = json.load(open('%s/data/news.json' % (settings.PROJECT_ROOT)))
        for n in doc[:200]:
            #print(json.dumps(n,indent=4,sort_keys=True))
            
            # Not handling: game
            
            news = News.objects.create(
                title=n['headline'],
                description=n['news'],
                reporter=n['user'],
                created_date = n['timestamp'],
                updated_date = n['timestamp']
            )
            news.tags.add('cat:%s' % (n['newstype']))
            for l in n['comments']:
                com = Comment.objects.create(
                    created_date = l['timestamp'],
                    updated_date = l['timestamp'],
                    description = l['comment'],
                    entity = news,
                    title = l['subject'],
                    reporter = l['user']
                )
                sub_comments(news, com, l['comments'])

            count = count+1
            if count==100:
                sys.stdout.write('.')
                sys.stdout.flush()
                count=0
                transaction.commit()

        print('')                
        transaction.commit()