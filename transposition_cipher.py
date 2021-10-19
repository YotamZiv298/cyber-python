def encrypt(key, txt):
    encrypted_txt = [''] * key

    for col in range(key):
        curr_index = col

        while curr_index < len(txt):
            encrypted_txt[col] += txt[curr_index]
            curr_index += key

    return ''.join(encrypted_txt)


def main():
    texts = ['Underneath(s)a(s)huge(s)oak(s)tree(s)there(s)was(s)of(s)swine(s)a(s)huge(s)company',
             'That(s)grunted(s)as(s)they(s)crunched(s)the(s)mast:(s)'
             'For(s)that(s)was(s)ripe,(s)and(s)fell(s)full(s)fast.',
             'Then(s)they(s)trotted(s)away,(s)for(s)the(s)wind(s)grew(s)high:(s)'
             'One(s)acorn(s)they(s)left,(s)and(s)no(s)more(s)might(s)you(s)spy']
    key = 9

    for text in texts:
        print(encrypt(key, text))


if __name__ == '__main__':
    main()
