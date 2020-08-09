#lang racket

; This is an exercise program in <SICP> CH3.
; Mainly about simple variables and systems.
; Author : Brethland, Late 2019.

(define (equal? a b)
    (cond ((and (not (pair? a)) (not (pair? b))) (eq? a b))
          ((or (not (pair? a)) (not (pair? b))) #f)
          (else (and (equal? (car a) (car b)) (equal? (cdr a) (cdr b))))))
(define (element-of-set? x set)
    (cond ((null? set) #f)
          ((equal? x (car set)) #t)
          (else (element-of-set? x (cdr set)))))
(define (adjoin-set x set)
    (cons x set))
(define (factorial n)
    (cond ((= n 0) 1)
          (else (* n (factorial (- n 1))))))
(define (make-accumulator iter)
    (lambda (addend)
        (begin (set! iter (+ iter addend))
            iter)))
(define A (make-accumulator 10))
; (A 10)
; (A (- 10))
(define (make-monitored f)
    (let ((encounter 0))
    (define (how-many-calls?)
        encounter)
    (define (reset-count)
        (set! encounter 0))
    (define (dispatch m)
        (cond ((eq? m `how-many-calls?) (how-many-calls?))
              ((eq? m `reset-count) (reset-count))
              (else (begin (set! encounter (+ encounter 1)) (f m)))))
    dispatch))
(define fac (make-monitored factorial))
; (fac 5)
; (fac `how-many-calls?)
; (fac `reset-count)
; (fac 7)
; (fac `how-many-calls?)
(define (make-account balance password)
    (let ((wrong-doings 0)
          (secret (list password)))
    (define (withdraw amount)
        (if (>= balance amount)
            (begin (set! balance (- balance amount))
                balance)
            "Insufficient funds"))
    (define (deposit amount)
        (set! balance (+ balance amount))
        balance)
    (define (dispatch pass m)
        (cond ((not (element-of-set? pass secret)) 
            (if (< wrong-doings 6)
            (begin (set! wrong-doings (+ wrong-doings 1)) (lambda (money) (display "Incorrect Password")))
            (lambda (money) (display "Call the Police!"))))
              (else (cond ((eq? m `withdraw) withdraw)
                          ((eq? m `deposit) deposit)
                          ((eq? m `join) (lambda (new-pass) (set! secret (cons new-pass secret))))
                          (else (display "Unknown request -- MAKE-ACCOUNT" m))))))
    dispatch))
(define (make-joint account secret new-pass)
    (begin ((account secret `join) new-pass) account))
(define acc (make-account 100 `admin))
(define paul-acc (make-joint acc `admin `guest))
((paul-acc `guest `withdraw) 10)
(define (random-in-range low high)
    (let ((range (- high low)))
        (+ low (* (random) range))))
(define (estimate-integral p x1 x2 y1 y2 trial-times)
    (define (exp)
        (p (random-in-range x1 x2) (random-in-range y1 y2)))
    (define (monte-carlo trials experiment)
        (define (iter trials-remaining trials-passed)
            (cond ((= trials-remaining 0) (/ trials-passed trials))
                ((experiment) (iter (- trials-remaining 1) (+ trials-passed 1)))
                (else (iter (- trials-remaining 1) trials-passed))))
        (iter trials 0))
    (let ((estimate-rate (monte-carlo trial-times exp)))
        (* estimate-rate (* (- x2 x1) (- y2 y1)))))
(define unit-circle
    (lambda (x y)
        (<= 1.0 (+ (* x x) (* y y)))))
; (estimate-integral unit-circle (- 1.0) 1.0 (- 1.0) 1.0 1000000)
(define random
    (let ((x 114514))
    (define generate
        (begin (set! x (random-update x))
            x))
    (define reset
        (lambda (m) (set! x m)))
    (define (dispatch m)
        (cond ((eq? m `generate) generate)
              ((eq? m `reset) reset)
              (else (display "Unknown operation -- Rand" m))))
    dispatch))

(define (f m)
    (let ((x 0))
        (begin x (set! x m))))