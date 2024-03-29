#coding: utf-8

from django.core.management.base import BaseCommand, CommandError

from catalogo.models import Publicacao
from catalogo.isbn import validatedISBN10
from django.utils.text import Truncator

class Command(BaseCommand):
    help = (u'Verifica se o id_padrao dos livros é um ISBN válido\n' +
            u'(use alterar_tipo para mudar tipo para "outro" se o ISBN é inválido)')
    def handle(self, *args, **options):
        self.stdout.write('Verificando ISBN nos registros de Publicacao\n')
        qt_registros = Publicacao.objects.filter(tipo='livro').count()
        self.stdout.write('%s registros de Publicacao encontrados\n' % qt_registros)
        qt_isbn_invalidos = 0
        alterar_tipo = 'alterar_tipo' in args
        for reg in Publicacao.objects.filter(tipo = 'livro'):
            isbn_ok = validatedISBN10(reg.id_padrao)
            if isbn_ok:
                continue
            qt_isbn_invalidos += 1
            titulo_abrev = Truncator(reg.titulo).chars(60)
            linha = u'{0} {1} {2}\n'.format(reg.id, reg.id_padrao, titulo_abrev)
            linha = linha.encode('utf-8')
            self.stdout.write(linha)
            if 'alterar_tipo' in args:
                reg.tipo = u'outro'
                reg.save()
        self.stdout.write('%s registros com ISBN inválidos\n' % qt_isbn_invalidos)
        if alterar_tipo and qt_isbn_invalidos > 0:
            self.stdout.write('TIPOS ALTERADOS PARA "outro"\n')
            
