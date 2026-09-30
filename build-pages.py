#!/usr/bin/env python3
"""Builds the legal pages of the site (privacy, terms, account deletion) in English and French
from the content below, so both languages keep the same structure. Run from the repo root:
`python3 site/build-pages.py`. Commit the generated HTML with this file.

Facts come from the app and backend (docs/TECH.md, supabase/migrations): change them here when
what Darna collects, where it's stored or how long it's kept changes.
"""
from pathlib import Path

SITE = Path(__file__).parent
UPDATED = {'en': 'September 30, 2026', 'fr': '30 septembre 2026'}
PUBLISHER = 'MLB Tech Solutions'
# TODO(owner): the registered address of MLB Tech Solutions.
ADDRESS = '[registered address to add]'
CONTACT = 'support@mlb-techsolutions.com'

PAGES = {
    'privacy': {
        'en': {
            'title': 'Privacy policy',
            'lead': f'Darna is a shared household app: lists, tasks, calendar, meals, budget and a family map. This policy explains what data Darna uses, why, who can see it and how long it is kept. In short: your household sees what you share with it, we don’t sell or rent anything, and there are no ads or trackers.',
            'body': f"""
<h2>Who is responsible</h2>
<p>{PUBLISHER}, {ADDRESS}, publishes Darna and is the data controller. For anything about your data, write to <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>

<h2>What Darna uses</h2>
<ul>
<li><strong>Your account:</strong> your email address (to send you sign-in codes), your name, your photo if you add one, your language and appearance settings, and whether you are 16 or older (asked once, so younger people join a parent’s home as a child).</li>
<li><strong>What you add to a home:</strong> lists and items (with a price or a photo if you add them), tasks and who did them, calendar events and who attends, meals and recipes, expenses, splits, budgets and recurring bills, saved places, and the home’s activity feed.</li>
<li><strong>Your location, only if you turn sharing on:</strong> your latest position, shown to the adults of your home, and arrivals at and departures from the places your home saved (with Darna+ place alerts). You can pause or stop sharing at any time; stopping deletes your position from our servers. Sharing while Darna is closed is a separate choice, and needs your phone’s “always” permission.</li>
<li><strong>Your phone, for notifications:</strong> a push token and this phone’s notification settings (topics, quiet hours, language and time zone), so we can tell you what happens at home.</li>
<li><strong>Things that stay on your phone:</strong> your phone’s calendars (if you choose to show them next to the household’s) are read on the phone only and never sent to us. The camera is used to scan an invite QR code or take a photo you choose to add.</li>
</ul>
<p>Darna has no advertising, no analytics trackers and no session recording.</p>

<h2>Why we use it</h2>
<ul>
<li>To provide the service you asked for: your account, your homes and what you share in them (performance of a contract).</li>
<li>Location, notifications, camera and calendars only with your permission, which you can withdraw in your phone’s settings (consent).</li>
<li>To keep Darna safe, for example by limiting repeated sign-in and invite code attempts (legitimate interest).</li>
</ul>

<h2>Who can see it</h2>
<ul>
<li><strong>The members of each home</strong> see what is shared in that home. Money (expenses, balances, budgets) and other members’ positions are shown to adults only, never on a child’s phone.</li>
<li><strong>Our service providers,</strong> only to run Darna on our behalf:
  <ul>
  <li>Supabase (database, sign-in, photo storage) and PowerSync (keeping phones in sync), in the European Union.</li>
  <li>Resend, which sends the sign-in code emails, in the United States.</li>
  <li>Expo and Google Firebase Cloud Messaging, which deliver push notifications, in the United States.</li>
  <li>Mapbox (or OpenStreetMap), which serves the map images: your phone asks for the part of the map on screen, so they receive your IP address and that area, not who you are.</li>
  <li>GitHub, which hosts this website.</li>
  </ul>
  Transfers outside the EU rely on the European Commission’s standard contractual clauses or the EU-US Data Privacy Framework.</li>
</ul>
<p>We don’t sell, rent or share your data for advertising.</p>

<h2>How long we keep it</h2>
<ul>
<li>Your account and what you added: until you delete your account (see below) or leave a home.</li>
<li>Positions and place visits: 30 days at most, and positions are deleted as soon as you stop sharing.</li>
<li>The activity feed: 30 days.</li>
<li>Notifications waiting to be sent: 7 days. Security records (wrong invite codes): 1 day.</li>
</ul>

<h2>Children</h2>
<p>Under 16, you can’t create a home: a parent creates it and invites you, and you join as a child. Parents can also add a child profile without an account (a name, and a photo if they add one). Children’s phones never receive money data or other members’ positions.</p>

<h2>Your rights</h2>
<p>You can access, correct, export and delete your data, object to or restrict some uses, and withdraw a permission at any time.</p>
<ul>
<li><strong>Export:</strong> Settings → Export my data gives you a copy of everything you added.</li>
<li><strong>Correct:</strong> change your name, photo and settings in the app.</li>
<li><strong>Delete:</strong> see <a href="{{prefix}}/delete-account">how to delete your account</a>.</li>
</ul>
<p>For anything else, write to <a href="mailto:{CONTACT}">{CONTACT}</a>; we answer within a month. You can also complain to your data protection authority (in France, the CNIL: <a href="https://www.cnil.fr">cnil.fr</a>).</p>

<h2>Security</h2>
<p>Data travels encrypted (HTTPS). Every read and write is checked on our servers against the rules of your home. On your phone, your sign-in is kept in the phone’s secure storage (Keychain or Keystore).</p>

<h2>Changes</h2>
<p>If this policy changes in a way that matters, we’ll tell you in the app before it applies.</p>
""",
        },
        'fr': {
            'title': 'Politique de confidentialité',
            'lead': 'Darna est une app partagée pour la maison : listes, tâches, agenda, repas, budget et carte familiale. Cette politique explique quelles données Darna utilise, pourquoi, qui peut les voir et combien de temps elles sont gardées. En bref : votre maison voit ce que vous partagez avec elle, nous ne vendons ni ne louons rien, et il n’y a ni publicité ni traceurs.',
            'body': f"""
<h2>Qui est responsable</h2>
<p>{PUBLISHER}, {ADDRESS}, publie Darna et est responsable du traitement. Pour toute question sur vos données, écrivez à <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>

<h2>Ce que Darna utilise</h2>
<ul>
<li><strong>Votre compte :</strong> votre adresse e-mail (pour vous envoyer les codes de connexion), votre nom, votre photo si vous en ajoutez une, vos réglages de langue et d’apparence, et si vous avez 16 ans ou plus (demandé une fois, pour que les plus jeunes rejoignent la maison d’un parent comme enfant).</li>
<li><strong>Ce que vous ajoutez à une maison :</strong> listes et articles (avec un prix ou une photo si vous en ajoutez), tâches et qui les a faites, événements de l’agenda et qui y participe, repas et recettes, dépenses, partages, budgets et factures récurrentes, lieux enregistrés, et le fil d’activité de la maison.</li>
<li><strong>Votre position, seulement si vous activez le partage :</strong> votre dernière position, visible par les adultes de votre maison, et vos arrivées et départs des lieux enregistrés par la maison (avec les alertes de lieux Darna+). Vous pouvez mettre en pause ou arrêter le partage à tout moment ; l’arrêter supprime votre position de nos serveurs. Partager quand Darna est fermée est un choix à part, qui demande l’autorisation « toujours » de votre téléphone.</li>
<li><strong>Votre téléphone, pour les notifications :</strong> un jeton push et les réglages de notification de ce téléphone (sujets, heures calmes, langue et fuseau horaire), pour vous prévenir de ce qui se passe à la maison.</li>
<li><strong>Ce qui reste sur votre téléphone :</strong> les agendas de votre téléphone (si vous choisissez de les afficher à côté de celui de la maison) sont lus sur le téléphone uniquement et ne nous sont jamais envoyés. L’appareil photo sert à scanner un QR code d’invitation ou à prendre une photo que vous choisissez d’ajouter.</li>
</ul>
<p>Darna n’a ni publicité, ni traceurs d’analyse, ni enregistrement de session.</p>

<h2>Pourquoi nous les utilisons</h2>
<ul>
<li>Pour fournir le service demandé : votre compte, vos maisons et ce que vous y partagez (exécution du contrat).</li>
<li>La position, les notifications, l’appareil photo et les agendas seulement avec votre autorisation, que vous pouvez retirer dans les réglages du téléphone (consentement).</li>
<li>Pour protéger Darna, par exemple en limitant les tentatives répétées de connexion ou de code d’invitation (intérêt légitime).</li>
</ul>

<h2>Qui peut les voir</h2>
<ul>
<li><strong>Les membres de chaque maison</strong> voient ce qui est partagé dans cette maison. L’argent (dépenses, soldes, budgets) et la position des autres membres ne sont montrés qu’aux adultes, jamais sur le téléphone d’un enfant.</li>
<li><strong>Nos prestataires,</strong> uniquement pour faire fonctionner Darna pour notre compte :
  <ul>
  <li>Supabase (base de données, connexion, stockage des photos) et PowerSync (synchronisation des téléphones), dans l’Union européenne.</li>
  <li>Resend, qui envoie les e-mails de code de connexion, aux États-Unis.</li>
  <li>Expo et Google Firebase Cloud Messaging, qui acheminent les notifications push, aux États-Unis.</li>
  <li>Mapbox (ou OpenStreetMap), qui fournit les images de la carte : votre téléphone demande la partie de carte affichée, ils reçoivent donc votre adresse IP et cette zone, pas votre identité.</li>
  <li>GitHub, qui héberge ce site.</li>
  </ul>
  Les transferts hors de l’UE reposent sur les clauses contractuelles types de la Commission européenne ou le cadre de protection des données UE–États-Unis.</li>
</ul>
<p>Nous ne vendons pas, ne louons pas et ne partageons pas vos données à des fins publicitaires.</p>

<h2>Combien de temps nous les gardons</h2>
<ul>
<li>Votre compte et ce que vous avez ajouté : jusqu’à la suppression de votre compte (voir plus bas) ou votre départ d’une maison.</li>
<li>Positions et passages dans les lieux : 30 jours au plus, et les positions sont supprimées dès que vous arrêtez le partage.</li>
<li>Le fil d’activité : 30 jours.</li>
<li>Notifications en attente d’envoi : 7 jours. Traces de sécurité (codes d’invitation erronés) : 1 jour.</li>
</ul>

<h2>Enfants</h2>
<p>Avant 16 ans, vous ne pouvez pas créer de maison : un parent la crée et vous invite, et vous la rejoignez comme enfant. Les parents peuvent aussi ajouter un profil enfant sans compte (un nom, et une photo s’ils en ajoutent une). Les téléphones des enfants ne reçoivent jamais les données d’argent ni la position des autres membres.</p>

<h2>Vos droits</h2>
<p>Vous pouvez accéder à vos données, les corriger, les exporter et les supprimer, vous opposer à certains usages ou les limiter, et retirer une autorisation à tout moment.</p>
<ul>
<li><strong>Exporter :</strong> Réglages → Exporter mes données vous donne une copie de tout ce que vous avez ajouté.</li>
<li><strong>Corriger :</strong> modifiez votre nom, votre photo et vos réglages dans l’app.</li>
<li><strong>Supprimer :</strong> voir <a href="{{prefix}}/delete-account">comment supprimer votre compte</a>.</li>
</ul>
<p>Pour tout le reste, écrivez à <a href="mailto:{CONTACT}">{CONTACT}</a> ; nous répondons sous un mois. Vous pouvez aussi saisir l’autorité de protection des données (en France, la CNIL : <a href="https://www.cnil.fr">cnil.fr</a>).</p>

<h2>Sécurité</h2>
<p>Les données circulent chiffrées (HTTPS). Chaque lecture et écriture est vérifiée sur nos serveurs selon les règles de votre maison. Sur votre téléphone, votre connexion est gardée dans le stockage sécurisé du téléphone (Trousseau ou Keystore).</p>

<h2>Modifications</h2>
<p>Si cette politique change de manière importante, nous vous prévenons dans l’app avant que le changement s’applique.</p>
""",
        },
    },
    'terms': {
        'en': {
            'title': 'Terms of use',
            'lead': 'These terms apply when you use Darna. They are short on purpose.',
            'body': f"""
<h2>The service</h2>
<p>Darna, published by {PUBLISHER} ({ADDRESS}), lets the members of a household share lists, tasks, a calendar, meals, a budget and, if they choose, their location. Darna is in early testing: features may change, and occasional bugs are possible.</p>

<h2>Your account</h2>
<ul>
<li>You sign in with a code sent to your email address. Keep access to that address to yourself.</li>
<li>Under 16, you join a home created by a parent, as a child.</li>
<li>You are responsible for what you add to Darna. Only add photos and content you have the right to share, and nothing illegal or hurtful.</li>
<li>The admin of a home can invite and remove members and change their roles.</li>
</ul>

<h2>Darna+</h2>
<p>Darna+ is an optional subscription for the whole household. It starts with a free trial, then renews automatically at the price shown before you subscribe, until you cancel. You cancel in your App Store or Google Play subscriptions, at least 24 hours before it renews. The store’s refund rules apply.</p>

<h2>Location and safety</h2>
<p>Positions and place alerts depend on your phone, its settings and its connection. They can be late or missing: never rely on Darna alone for someone’s safety.</p>

<h2>Your content</h2>
<p>What you add stays yours. You allow us to store it and show it to the members of the homes you share it with, only to run Darna. The <a href="{{prefix}}/privacy">privacy policy</a> explains how we handle your data.</p>

<h2>Ending</h2>
<p>You can leave a home or <a href="{{prefix}}/delete-account">delete your account</a> at any time. We may suspend an account that breaks these terms, after telling you when we can.</p>

<h2>Liability</h2>
<p>We do our best to keep Darna available and your data safe, but Darna is provided as is, without a guarantee that it will always work without interruption. Nothing in these terms limits the rights consumers have under the law.</p>

<h2>Law and contact</h2>
<p>These terms are governed by French law. Questions: <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
""",
        },
        'fr': {
            'title': 'Conditions d’utilisation',
            'lead': 'Ces conditions s’appliquent quand vous utilisez Darna. Elles sont courtes exprès.',
            'body': f"""
<h2>Le service</h2>
<p>Darna, publiée par {PUBLISHER} ({ADDRESS}), permet aux membres d’une maison de partager des listes, des tâches, un agenda, des repas, un budget et, s’ils le souhaitent, leur position. Darna est en phase de test : des fonctionnalités peuvent changer et des bugs sont possibles.</p>

<h2>Votre compte</h2>
<ul>
<li>Vous vous connectez avec un code envoyé à votre adresse e-mail. Gardez l’accès à cette adresse pour vous.</li>
<li>Avant 16 ans, vous rejoignez une maison créée par un parent, comme enfant.</li>
<li>Vous êtes responsable de ce que vous ajoutez à Darna. N’ajoutez que des photos et contenus que vous avez le droit de partager, et rien d’illégal ou de blessant.</li>
<li>L’administrateur d’une maison peut inviter et retirer des membres et changer leurs rôles.</li>
</ul>

<h2>Darna+</h2>
<p>Darna+ est un abonnement facultatif pour toute la maison. Il commence par un essai gratuit, puis se renouvelle automatiquement au prix affiché avant l’abonnement, jusqu’à ce que vous l’annuliez. Vous l’annulez dans vos abonnements App Store ou Google Play, au moins 24 heures avant le renouvellement. Les règles de remboursement du store s’appliquent.</p>

<h2>Position et sécurité</h2>
<p>Les positions et alertes de lieux dépendent de votre téléphone, de ses réglages et de sa connexion. Elles peuvent arriver en retard ou manquer : ne comptez jamais uniquement sur Darna pour la sécurité de quelqu’un.</p>

<h2>Votre contenu</h2>
<p>Ce que vous ajoutez reste à vous. Vous nous autorisez à le stocker et à le montrer aux membres des maisons avec qui vous le partagez, uniquement pour faire fonctionner Darna. La <a href="{{prefix}}/privacy">politique de confidentialité</a> explique comment nous traitons vos données.</p>

<h2>Arrêter</h2>
<p>Vous pouvez quitter une maison ou <a href="{{prefix}}/delete-account">supprimer votre compte</a> à tout moment. Nous pouvons suspendre un compte qui enfreint ces conditions, en vous prévenant quand c’est possible.</p>

<h2>Responsabilité</h2>
<p>Nous faisons de notre mieux pour que Darna reste disponible et vos données en sécurité, mais Darna est fournie telle quelle, sans garantie de fonctionnement sans interruption. Rien dans ces conditions ne limite les droits que la loi accorde aux consommateurs.</p>

<h2>Droit applicable et contact</h2>
<p>Ces conditions sont régies par le droit français. Questions : <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
""",
        },
    },
    'delete-account': {
        'en': {
            'title': 'Delete your Darna account',
            'lead': 'You can delete your account and your data at any time, in the app or by email.',
            'body': f"""
<h2>In the app</h2>
<ol>
<li>Open Darna and tap your photo at the top of Home to open Settings.</li>
<li>Tap <strong>Delete my account</strong> and confirm.</li>
</ol>
<p>If you are the admin of a home that has other adults, make one of them admin first (tap them in Family → Make admin): the home stays with them.</p>

<h2>Without the app</h2>
<p>Write to <a href="mailto:{CONTACT}?subject=Delete%20my%20Darna%20account">{CONTACT}</a> from the email address you sign in with, asking us to delete your account. We do it within 30 days and confirm by email.</p>

<h2>What is deleted, and what stays</h2>
<ul>
<li><strong>Deleted:</strong> your account, profile and photo, your positions and place visits, your push registrations, and every home where nobody else has an account, with everything in it (lists, tasks, calendar, meals, budget, photos).</li>
<li><strong>Stays in homes you share with others:</strong> what you added there (a list item, an event, an expense) so the rest of the household keeps its history, without your name.</li>
<li>Copies in our providers’ backups are deleted when those backups expire, within 30 days.</li>
</ul>
<p>Want a copy first? Settings → <strong>Export my data</strong>.</p>
""",
        },
        'fr': {
            'title': 'Supprimer votre compte Darna',
            'lead': 'Vous pouvez supprimer votre compte et vos données à tout moment, dans l’app ou par e-mail.',
            'body': f"""
<h2>Dans l’app</h2>
<ol>
<li>Ouvrez Darna et touchez votre photo en haut de l’accueil pour ouvrir les Réglages.</li>
<li>Touchez <strong>Supprimer mon compte</strong> et confirmez.</li>
</ol>
<p>Si vous administrez une maison où il y a d’autres adultes, nommez d’abord l’un d’eux administrateur (touchez-le dans Famille → Nommer admin) : la maison reste avec eux.</p>

<h2>Sans l’app</h2>
<p>Écrivez à <a href="mailto:{CONTACT}?subject=Supprimer%20mon%20compte%20Darna">{CONTACT}</a> depuis l’adresse e-mail avec laquelle vous vous connectez, pour demander la suppression de votre compte. Nous le faisons sous 30 jours et vous le confirmons par e-mail.</p>

<h2>Ce qui est supprimé, et ce qui reste</h2>
<ul>
<li><strong>Supprimé :</strong> votre compte, votre profil et votre photo, vos positions et passages dans les lieux, vos inscriptions aux notifications, et chaque maison où personne d’autre n’a de compte, avec tout son contenu (listes, tâches, agenda, repas, budget, photos).</li>
<li><strong>Reste dans les maisons partagées avec d’autres :</strong> ce que vous y avez ajouté (un article, un événement, une dépense), pour que la maison garde son historique, sans votre nom.</li>
<li>Les copies dans les sauvegardes de nos prestataires sont supprimées à l’expiration de ces sauvegardes, sous 30 jours.</li>
</ul>
<p>Vous voulez une copie avant ? Réglages → <strong>Exporter mes données</strong>.</p>
""",
        },
    },
}

LABELS = {
    'en': {'updated': 'Last updated', 'other': 'Français', 'home': 'Darna', 'privacy': 'Privacy', 'terms': 'Terms', 'delete': 'Delete account'},
    'fr': {'updated': 'Dernière mise à jour', 'other': 'English', 'home': 'Darna', 'privacy': 'Confidentialité', 'terms': 'Conditions', 'delete': 'Supprimer le compte'},
}

TEMPLATE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Darna</title>
<link rel="stylesheet" href="/style.css">
</head>
<body>
<header><a class="brand" href="/"><img src="/logo.png" alt="" width="32" height="32">Darna</a><a class="lang" href="{other_href}" hreflang="{other_lang}">{other}</a></header>
<main>
<h1>{title}</h1>
<p class="updated">{updated}: {date}</p>
<p class="lead">{lead}</p>
{body}
</main>
<footer><a href="{prefix}/privacy">{l_privacy}</a> · <a href="{prefix}/terms">{l_terms}</a> · <a href="{prefix}/delete-account">{l_delete}</a> · <a href="mailto:{contact}">{contact}</a></footer>
</body>
</html>
"""

for slug, langs in PAGES.items():
    for lang, page in langs.items():
        prefix = '' if lang == 'en' else '/fr'
        other_lang = 'fr' if lang == 'en' else 'en'
        other_prefix = '' if other_lang == 'en' else '/fr'
        l = LABELS[lang]
        html = TEMPLATE.format(
            lang=lang, title=page['title'], lead=page['lead'], body=page['body'].strip().replace('{prefix}', prefix),
            updated=l['updated'], date=UPDATED[lang], other=l['other'], other_lang=other_lang, other_href=f'{other_prefix}/{slug}',
            prefix=prefix, l_privacy=l['privacy'], l_terms=l['terms'], l_delete=l['delete'], contact=CONTACT,
        )
        out = SITE / (f'{slug}.html' if lang == 'en' else f'fr/{slug}.html')
        out.parent.mkdir(exist_ok=True)
        out.write_text(html, encoding='utf-8')
        print('wrote', out.relative_to(SITE))
