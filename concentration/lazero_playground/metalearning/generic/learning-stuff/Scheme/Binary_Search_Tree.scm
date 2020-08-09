#lang racket

; This is an program implementing BST Data structures.
; Some code comes from <SICP>
; Author : Brethland, Early 2019.

(define (entry tree) (car tree))
(define (left-branch tree) (car (cdr tree)))
(define (right-branch tree) (car (cdr (cdr tree))))
(define (make-tree entry left-tree right-tree) (list entry left-tree right-tree))
(define (tree->list tree)
    (define (copy-to-list tree result-tree)
        (if (null? tree)
            result-tree
            (copy-to-list (left-branch tree)
                (cons (entry tree) (copy-to-list (right-branch tree) result-tree)))))
    (copy-to-list tree `()))
(define (list->tree elements)
    (car (partial-tree elements (length elements))))
(define (partial-tree elts n)
    (if (= n 0)
        (cons`() elts)
        (let ((left-size (quotient (- n 1) 2)))
            (let ((left-result (partial-tree elts left-size)))
                (let ((left-tree (car left-result))
                      (non-left-elts (cdr left-result))
                      (right-size (- n (+ left-size 1))))
                    (let ((this-entry (car non-left-elts))
                          (right-result (partial-tree (cdr non-left-elts) right-size)))
                        (let ((right-tree (car right-result))
                              (remaining-elts (cdr right-result)))
                            (cons (make-tree this-entry left-tree right-tree) remaining-elts))))))))
(define (union-set set1 set2)
    (cond ((null? set1) set2)
          ((null? set2) set1)
          (else (let ((x1 (car set1))
                      (x2 (car set2)))
                      (cond ((= x1 x2) (cons x1 (union-set (cdr set1) (cdr set2))))
                            ((< x1 x2) (cons x1 (union-set (cdr set1) set2)))
                            (else (cons x2 (union-set set1 (cdr set2)))))))))
(define (intersection-set set1 set2)
    (cond ((or (null? set2) (null? set1)) `())
          (else (let ((x1 (car set1))
                      (x2 (car set2)))
                      (cond ((= x1 x2) (cons x1 (intersection-set (cdr set1) (cdr set2))))
                            ((< x1 x2) (intersection-set (cdr set1) set2))
                            (else (intersection-set set1 (cdr set2))))))))
(define (intersection-tree tree1 tree2)
    (let ((set1 (tree->list tree1))
          (set2 (tree->list tree2)))
        (list->tree (intersection-set set1 set2))))
(define (union-tree tree1 tree2)
    (let ((set1 (tree->list tree1))
          (set2 (tree->list tree2)))
        (list->tree (union-set set1 set2))))
; (intersection-tree (list->tree (list 1 4 7 8 9)) (list->tree (list 2 5 7 9 10)))
; (union-tree (list->tree (list 1 4 7 8 9)) (list->tree (list 2 5 7 9 10)))
(define (look-up given-key set-of-records)
    (cond ((null? set-of-records) false)
          ((= given-key (entry set-of-records)) (entry-set-of-records))
          ((< given-key (entry-set-of-records)) (look-up given-key (left-branch set-of-records)))
          (else (look-up given-key (right-branch set-of-records)))))